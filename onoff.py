import RPi.GPIO as GPIO
from time import sleep
import off
GPIO.setmode(GPIO.BOARD)
while(1):
	x=input("enter pin no:  ")
	for k in range(0,2):
		y=input("enter 1 to on 0 to off:  ")
		GPIO.setup(x,GPIO.OUT)
		GPIO.output(x,y)
