from functions import*
import numpy as np
import cv2
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
import datetime
print '\n',datetime.datetime.now(),'\n'
loc = 88 #176/2
scan_line_loc = [18,53,88,123,158]
oL1=[]
L1=[]
lastseen=[]
mw=255

#hostipadd="http://"+raw_input('enter ip address of host: ')+":8080/video"
hostipadd="http://192.168.0.101:8080/video"
cap = cv2.VideoCapture()
cap.open(hostipadd)

for x in range(0,90):
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print mw
    if max(grey[loc])-min(grey[loc])<70 and min(grey[loc])>100:
		if min(grey[loc])<mw : mw = min(grey[loc])
		
   
cap.release()
cv2.destroyAllWindows()
print '\n',datetime.datetime.now()
