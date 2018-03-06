import RPi.GPIO as GPIO
def off():
	import sys
	sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib/')
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	i=[3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26]
	for x in range(0,41):
		try:
			GPIO.setup(x,GPIO.OUT)
			GPIO.output(x,0)
		except:
			continue
off()
GPIO.cleanup()
