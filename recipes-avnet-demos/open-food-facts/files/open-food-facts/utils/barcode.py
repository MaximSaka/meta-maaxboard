#pip3 install evdev

import sys
import time
import threading
import glob

try:
	import evdev
	from evdev import InputDevice
	evdevAvailable = True
except:
	evdevAvailable = False

class BarcodeReader():
	# Provided as an example taken from my own keyboard attached to a Centos 6 box:
	scancodes = {
		# Scancode: ASCIICode
		0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
		10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
		20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
		30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
		40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
		50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
	}

	def __init__(self, callback = None):
		global evdevAvailable

		self.dev=None
		self.barcodeValue = ''
		self.callback = callback
		self.evdevAvailable = evdevAvailable

		try:
			HIDThread = threading.Thread(target=self.ReadBarcode)
			HIDThread.start()
		except:
			self.evdevAvailable = False

		STDINThread = threading.Thread(target=self.ReadBarcodeKeyboard)
		STDINThread.start()

	def ConnectToReader(self):
		try:
			# barcode reader HID 0581:011c
			eventList = glob.glob('/dev/input/event*')

			for x in range(len(eventList)):
				self.dev = InputDevice(eventList[x])
				if 'HID 0581:011c' in self.dev.name:
					print(self.dev)
					print("found reader")
					break
		except:
			self.dev = None

	def GetBarcode(self):
		newBarcode = self.barcodeValue.strip()
		self.barcodeValue = ''
		if self.callback != None:
			self.callback(newBarcode)
		return newBarcode
	
	def ReadBarcode(self):
		while True:
			if(self.dev == None):
				self.ConnectToReader()
				time.sleep(1)
				continue

			try:
				barcodeTemp = ''
				for event in self.dev.read_loop():
					if event.type == evdev.ecodes.EV_KEY:
						data = evdev.categorize(event)  # Save the event temporarily to introspect it
						if data.keystate == 1:  # Down events only
							key_lookup = self.scancodes.get(data.scancode) or u'UNKNOWN:{}'.format(data.scancode)  # Lookup or return UNKNOWN:XX
							#print (key_lookup)  # Print it all out!

							if(key_lookup == 'CRLF'):
								self.barcodeValue = barcodeTemp
								barcodeTemp = ''
								self.GetBarcode()
							else:
								barcodeTemp = barcodeTemp + key_lookup

			except:
				self.dev = None

			time.sleep(1)

	def ReadBarcodeKeyboard(self):
		while True:
			try:
				self.barcodeValue = sys.stdin.readline()
				self.GetBarcode()
			except:
				pass

			time.sleep(1)


# Sample test logic
#reader = BarcodeReader()
#while True:
#	barcodevalue = reader.GetBarcode().strip()
#	if(barcodevalue != ''):
#		print('newbarcode:' + barcodevalue)
#	time.sleep(1)
	
#def myCallBack(newBarcode):
#	print('newbarcode:' + newBarcode)
#	
#reader = BarcodeReader(myCallBack)
#while True:
#	continue
