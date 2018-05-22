import time
import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (560,420)
    camera.led = False
#    camera.color_effects = (128,128)
    camera.framerate=90
    time.sleep(1)
    while(1):	
		with picamera.array.PiRGBArray(camera) as stream:
			e1 = cv2.getTickCount()
			camera.capture(stream, format='bgr',use_video_port = True)
			# At this point the image is available as stream.array
			image = stream.array
		cv2.imshow('frame',image)
		print len(image),len(image[0]),image[0][0]
		e2 = cv2.getTickCount()
		time = 1/((e2 - e1)/ cv2.getTickFrequency())
		print time
		c = cv2.waitKey(7) % 0x100
		if c == 27:
			break
cv2.destroyAllWindows()

