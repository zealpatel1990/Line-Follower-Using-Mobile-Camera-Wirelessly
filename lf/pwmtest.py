import RPi.GPIO as GPIO
import off
from time import sleep

while(1):
	GPIO.setmode(GPIO.BOARD)
	pin = input("Enter pin number:-  ")
	freq = input("Input frequency:-  ")	
	GPIO.setup(pin, GPIO.OUT)
	pwm = GPIO.PWM(pin,freq)
	pwm.start(0)
	for k in range(0,6):
		print "pwm started."
		y = input("Enter Duty Cycle 0-100:-  ")
		pwm.ChangeDutyCycle(y)
	off.off()
	GPIO.cleanup()
