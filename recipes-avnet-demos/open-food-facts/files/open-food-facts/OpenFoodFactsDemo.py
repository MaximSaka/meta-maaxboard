#############################################################
# ___  ____ ____ ____ ____ ____ _  _ _ ____ _ ___ ____ ____ 
# |__] |__/ |___ |__/ |___ |  | |  | | [__  |  |  |___ [__  
# |    |  \ |___ |  \ |___ |_\| |__| | ___] |  |  |___ ___] 
#                                                           
#############################################################
#pip3 install openfoodfacts
#pip3 install microdot
#pip3 install evdev
#############################################################

#####################################################
#to stop teh service use this command
#systemctl stop  autorun.service
#####################################################

########################################################
#Options
########################################################
run_on_hardware = True

if run_on_hardware == False:
	HardwareSupport = False
	EnableUSBPowerMonitor = False
else:
	HardwareSupport = True
	EnableUSBPowerMonitor = True
########################################################
import os
import json
import subprocess
import json
import openfoodfacts

from utils.MaaXBoardLEDS import BoardLEDS
from utils.MaaXBoardLCD import BoardBrightness
from utils.barcode import BarcodeReader
import utils.singleton as singleton

try:
	import uasyncio as asyncio
except ImportError:
	import asyncio

from microdot_asyncio import Microdot, redirect, send_file

# will sys.exit(-1) if other instance is running
me = singleton.SingleInstance()

fileDir = os.path.dirname(os.path.realpath(__file__))

def GetFileFullPath(s):
	filePath = os.path.join(fileDir, s)
	filePath = os.path.abspath(os.path.realpath(filePath))
	return filePath

def startChrome(url):
	""" Calls Chrome, opening the URL contained in the url parameter. """

	if run_on_hardware == True:
		executable = '/usr/bin/chromium'
	else:
		executable = '/snap/bin/chromium'    # Change to fit your system

	cmd = ' '.join([executable,'--no-sandbox --disable-features=OverscrollHistoryNavigation --kiosk --app=', url])
	browswer_proc = subprocess.Popen(cmd, shell=True)

class AppData:
	def __init__(self):
		self.previousCode = ''
		self.barcode = ''
		self.productName = ''
		self.ingredients = ''
		self.image = ''
		self.allergens = ''
		self.nutriScore = ''
		self.novaScore = ''
	
	def ReaderCallback(self, barcode):
		self.barcode = barcode
		if self.barcode != self.previousCode:
			try:
				productInfo = openfoodfactsAPI.product.get(self.barcode)

				json_formatted_str = json.dumps(productInfo, indent=2)

				with open("product.json", "w") as outfile:
					outfile.write(json_formatted_str)

				json_str = json.loads(json_formatted_str)
				product_code = json_str.get("code")
			except:
				product_code = '0'
				pass

			if product_code != '0':
				product = json_str.get("product")

				try:
					self.productName = product["product_name"]
				except:
					self.productName ="Product name missing"

				try:
					self.ingredients = product["ingredients_text_en"]
				except:
					self.ingredients ="Not available"

				try:
					tempImage = product["selected_images"]["front"]["display"]
					firstKey = list(tempImage.keys())[0]
					print(firstKey)
					self.image = product["selected_images"]["front"]["display"][firstKey]
				except:
					self.image =''

				try:
					allergenList = product["allergens_hierarchy"]
				except:
					allergenList = None

				allergensString = ''
				for x in range(len(allergenList)):
					if 'en:' in allergenList[x]:
						allergensString = allergensString + allergenList[x].removeprefix('en:') + ', '
				self.allergens = allergensString[:-2] #remove extra comma from the end of the string
				if self.allergens == '':
					self.allergens = 'None'

				value = product.get("nutriscore_data")
				if value != None:
					self.nutriScore = value["grade"]

				value = product.get("nutriments")
				if value != None:
					self.novaScore = value["nova-group"]
			else: 
				self.productName = ''

			#self.previousCode = self.barcode
	

########################################################
app = Microdot()

@app.route('/product.cgi', methods=['GET'])
def power(request):

	response = None
	if request.method == 'GET':
		data_set = {"cmdType": 'product', 
			  "name": logic.productName,
			  "ingredients": logic.ingredients,
			  "allergens": logic.allergens,
			  "image": logic.image,
			  "nutriScore": logic.nutriScore,
			  "novaScore": logic.novaScore}

		product_cookie = json.dumps(data_set)
		response = product_cookie
	return response

@app.route('/<name>', methods=['GET', 'POST'])
def index(request,name):
	if request.method == 'POST':
		response = redirect('/')
	else:
		response = send_file(GetFileFullPath('web/'+name))

	return response

@app.route('/', methods=['GET', 'POST'])
def index(request):
	if request.method == 'POST':
		response = redirect('/')
	else:
		response = send_file(GetFileFullPath('web/index.html'))

	return response





openfoodfactsAPI = openfoodfacts.API(version="v2")

logic = AppData()

hardwareLEDS = BoardLEDS(HardwareSupport)
hardwareLEDS.LED_init()

hardwareLCD = BoardBrightness(HardwareSupport)
hardwareLCD.Brightness_init()

barcodeReader = BarcodeReader(logic.ReaderCallback)

startChrome('http://localhost:5000')

app.run(debug=False)

#sample code 			code = "3017620422003", "00014800210842", "54491014", "9002490205973 "

