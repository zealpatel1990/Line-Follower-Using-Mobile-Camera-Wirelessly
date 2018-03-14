#!/usr/bin/python
import io
import picamera
import cv2
import numpy as np
import sys
import math
import serial
from multiprocessing.dummy import Pool as ThreadPool
WINDOW_GRAY_IMAGE = 'gray image'
WINDOW_DISPLAY_IMAGE = 'display image'
CONTROL_SCAN_RADIUS = 'Scan Radius'
CONTROL_NUMBER_OF_CIRCLES = 'Number of Scans'
CONTROL_LINE_WIDTH = 'Line Width'
RESOLUTION_X = 160
RESOLUTION_Y = 120
SCAN_RADIUS = RESOLUTION_X / 4
SCAN_HEIGHT = RESOLUTION_Y - 10
SCAN_POS_X = RESOLUTION_X / 2
SCAN_RADIUS_REG = 25
NUMBER_OF_CIRCLES = 3
stream = io.BytesIO()
with picamera.PiCamera() as camera:
	camera.led=False # to turn off led on module
	camera.framerate = 30
	camera.resolution = (RESOLUTION_X, RESOLUTION_Y)
	while True:
		e1 = cv2.getTickCount()
		camera.capture(stream, format='jpeg', use_video_port=True)
		data = np.fromstring(stream.getvalue(), dtype=np.uint8)
		image = cv2.imdecode(data, cv2.CV_LOAD_IMAGE_COLOR)
		print len(image),len(image[0])
		grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
		display_image = cv2.copyMakeBorder(image, 0, 0, 0, 0, cv2.BORDER_REPLICATE)
		e2 = cv2.getTickCount()
		time = 1/((e2 - e1)/ cv2.getTickFrequency())
		print time
