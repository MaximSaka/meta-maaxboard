#############################################################
# ___  ____ ____ ____ ____ ____ _  _ _ ____ _ ___ ____ ____ 
# |__] |__/ |___ |__/ |___ |  | |  | | [__  |  |  |___ [__  
# |    |  \ |___ |  \ |___ |_\| |__| | ___] |  |  |___ ___] 
#                                                           
#############################################################
#pip3 install pyzbar
#pip3 install pydantic_core
#############################################################

#####################################################
#to stop teh service use this command
#systemctl stop  autorun.service
#####################################################

########################################################
#Options
########################################################
run_on_hardware = True

debug = False

if run_on_hardware == False:
	HardwareSupport = False
	EnableUSBPowerMonitor = False
	RotateCameraY = False
	RotateCameraX = False	
else:
	HardwareSupport = True
	EnableUSBPowerMonitor = True
	RotateCameraY = False
	RotateCameraX = False

########################################################
import os
import sys
import fnmatch
import cv2
import json
import subprocess
import openfoodfacts
from pyzbar.pyzbar import decode
import requests # request img from web
import shutil # save img locally

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
samplesDir = fileDir+'/samples'

global logic

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

def OpenCVDevice(self, useFile):
	try:
		if(self.cap.isOpened() == True):
			CloseCVDevice(self)
	except:
		pass
	
	if run_on_hardware == True:
		os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'hwaccel;qsv|video_codec;h264_qsv|vsync;0'
		self.cap = cv2.VideoCapture(cv2.CAP_V4L2)
	else:
		self.cap = cv2.VideoCapture(0)

	self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
	self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
	self.cap.set(cv2.CAP_PROP_FPS, 10)

def CloseCVDevice(self):
	try:
		self.cap.release()
	except:
		pass

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
		self.code = ''
	
	def DecodeFrame(self,frame):
		try:
			self.decoded = decode(frame)
		except: pass

		if len(self.decoded) > 0:
			if(self.decoded[0].data.decode() != self.previousCode):
				self.code = self.decoded[0].data.decode()
				self.ReaderCallback(self.code, "camera")

	def ReaderCallback(self, barcode, source):
		self.barcode = barcode
		if self.barcode != self.previousCode:
			self.previousCode = self.barcode

			if debug:
				print(source)
				print(self.barcode)

			#search in local samples first
			localFileFound = None
			jsonFound = None
			jpgFound = None
			for file in os.listdir(samplesDir):
				if fnmatch.fnmatch(file, '*'+self.barcode+'*.json'):
					jsonFound = samplesDir+'/'+file

				if fnmatch.fnmatch(file, '*'+self.barcode+'*.jpg'):
					jpgFound = samplesDir+'/'+file

			if (jpgFound != None) and (jsonFound != None):
				localFileFound = jsonFound

			try:
				if localFileFound == None:
					productInfo = openfoodfactsAPI.product.get(self.barcode)
				else:
					# Opening JSON file
					f = open(localFileFound)
					productInfo = json.load(f)

				json_formatted_str = json.dumps(productInfo, indent=2)

				json_str = json.loads(json_formatted_str)
				product_code = json_str.get("code")
			except:
				product_code = '0'
				pass

			if product_code != '0':
				product = json_str.get("product")

				if localFileFound == None:
					try:
						tempImage = product["selected_images"]["front"]["display"]
						firstKey = list(tempImage.keys())[0]
						self.image = product["selected_images"]["front"]["display"][firstKey]
					except:
						self.image =''

					if self.image != '' and debug:
						try:
							with open(samplesDir+'/'+self.barcode+".json", "w") as outfile:
								outfile.write(json_formatted_str)

							url = self.image
							onlineImage = requests.get(url, stream = True)
							image_file_name = samplesDir+'/'+self.barcode+".jpg"

							if onlineImage.status_code == 200:
								with open(image_file_name,'wb') as f:
									shutil.copyfileobj(onlineImage.raw, f)
						except: pass
				else:
					self.image = '/samples/'+os.path.basename(jpgFound)

				try:
					self.ingredients = product["ingredients_text_en"]
				except:
					pass

				if self.ingredients == '':
					try:
						self.ingredients = product["ingredients_text_"+firstKey]
					except:
						self.ingredients ="Not available"

				try:
					self.productName = product["product_name_en"]
				except:
					pass

				if self.productName == '':
					try:
						self.productName = product["product_name_"+firstKey]
					except:
						self.productName ="Product name missing"

				self.productName = self.productName + "\n\n #" + product_code

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
					try:
						self.nutriScore = value["grade"]
					except:
						self.nutriScore = None

				value = product.get("nutriments")
				if value != None:
					try:
						self.novaScore = value["nova-group"]
					except:
						self.novaScore = None

			else: 
				self.productName = ''


########################################################
app = Microdot()

@app.route('/video_feed')
async def video_feed(request):
	if sys.implementation.name != 'micropython':
		# CPython supports yielding async generators
		async def stream():
			yield b'--frame\r\n'
			OpenCVDevice(logic, False)
			while True:
				while (logic.cap.isOpened()):
					ret, frame = logic.cap.read()
					if ret:
						frame = frame[160:160+160, 160:160+320]
						frame = cv2.flip(frame, 0)
						frame = cv2.flip(frame, 1)

						detect_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
						logic.DecodeFrame(detect_frame)

						if len(logic.decoded) > 0:
							if logic.decoded[0].polygon is not None:
								if logic.decoded[0].data.decode() is not None:
									color=(0,0,255)
									thick=3
									(x, y, w, h) = logic.decoded[0].rect
									cv2.rectangle(frame, (x, y), (x + w, y + h), color, thick)

						_, frame = cv2.imencode('.JPEG', frame)
						yield (b'--frame\r\n'
							b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

					await asyncio.sleep(0.07)
				await asyncio.sleep(0.05)

	else:
		# MicroPython can only use class-based async generators
		class stream():
			def __init__(self):
				self.i = 0

			def __aiter__(self):
				return self

			async def __anext__(self):
				await asyncio.sleep(1)

	return stream(), 200, {'Content-Type':
						   'multipart/x-mixed-replace; boundary=frame'}

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

@app.route('/samples/<name>', methods=['GET', 'POST'])
def index(request,name):
	if request.method == 'POST':
		response = redirect('/')
	else:
		response = send_file(GetFileFullPath('samples/'+name))

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

#load a default product
logic.ReaderCallback('54491496', "init")

barcodeReader = BarcodeReader(logic.ReaderCallback)

startChrome('http://localhost:5000')

app.run(debug=False)

