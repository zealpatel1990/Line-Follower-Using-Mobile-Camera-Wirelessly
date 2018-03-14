from functions import*
import numpy as np
import cv2
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
import datetime
print '\n',datetime.datetime.now(),'\n'

#terms:- hor-horizontal; ver-vertical; len-length; pt-point;
#terms:- loc-location; oL-old line loc; L-new line loc; 

### variables
scan_line_loc = [18,53,88,123,158]
oL1=[];oL2=[];oL3=[];oL4=[];oL5=[]
L1=[];L2=[];L3=[];L4=[];L5=[]
rfpin=12;rbpin=16;lfpin=8;lbpin=10 #pins
GPIO.setup(rfpin,GPIO.OUT);GPIO.setup(rbpin,GPIO.OUT);GPIO.setup(lfpin,GPIO.OUT);GPIO.setup(lbpin,GPIO.OUT)
rf = GPIO.PWM(rfpin,100);rb = GPIO.PWM(rbpin,100);lf = GPIO.PWM(lfpin,100);lb = GPIO.PWM(lbpin,100);
rf.start(0);rb.start(0);lf.start(0);lb.start(0);
lastseen=[]
### end variables
############## functions start
def average(array):
    if len(array)>0:return sum(array)/len(array)
    else: return 0
def append(old_array,data,output_array):
    if old_array[0]-data<6 or old_array[len(old_array)-1]-data>-6 or old_array[0]==999:return output_array.append(data)
    else: return old_array
def checkarray(k):
    z=[];t=0
    avg = average(k)
    for x in k:
        z.append(abs(avg-x))
    avgz = average(z)
    for y in range(0,len(z)):
        if z[y]>avgz+8:
            del k[y-t]
            t+=1
    return k

def get_initial_black_line_array(array):
    thresold = average(array)/2;L=[]
    for j in range(0,len(array)):
            if array[j]<thresold:
                L.append(j)
    if len(L)==0: 
		L.append(999);
    return L
def get_black_line_array(array,oL):
    thresold = 200;L=[]#here thresold is not set average(array)/2
    for j in range(0,len(array)):
            if array[j]<thresold:
                append(oL,j,L)
    if len(L)==0: 
		L.append(999); 
		if oL[0]!=999: global lastseen; lastseen=oL;###point to be noted line is not found
    return L

def get_white_line_array(array,oL):
    thresold = 200;L=[]
    for j in range(0,len(array)):
            if array[j]>thresold:
                append(oL,j,L)
    if len(L)==0: L.append(999)###point to be noted line is not found
    return L
    
############## functions end

#hostipadd="http://"+raw_input('enter ip address of host: ')+":8080/video"
hostipadd="http://192.168.43.1:8080/video"
cap = cv2.VideoCapture()
cap.open(hostipadd)
hor_line_len = cap.get(3)
center_pt = hor_line_len/2 #ans:72--bcos 144 pixels
#here 176 hori. lines & 144 vertical lines

for x in range(0,9000):
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    L1=[];L2=[];L3=[];L4=[];L5=[]
    
    if x==0:
#        L1 = checkarray(get_initial_black_line_array(grey[scan_line_loc[0]]))
 #       L2 = checkarray(get_initial_black_line_array(grey[scan_line_loc[1]]))
  #      L3 = checkarray(get_initial_black_line_array(grey[scan_line_loc[2]]))
        L4 = checkarray(get_initial_black_line_array(grey[scan_line_loc[3]]))
        L5 = checkarray(get_initial_black_line_array(grey[scan_line_loc[4]]))
    #print center_pt,average(L1),average(L2),average(L3),average(L4),average(L5)
    else:
#        L1 = get_black_line_array(grey[scan_line_loc[0]],oL1)
 #       L2 = get_black_line_array(grey[scan_line_loc[1]],oL2)
  #      L3 = get_black_line_array(grey[scan_line_loc[2]],oL3)
        L4 = get_black_line_array(grey[scan_line_loc[3]],oL4)
        L5 = get_black_line_array(grey[scan_line_loc[4]],oL5)
    oL4=L4; oL5=L5
    pl5=average(L5);sl5=((center_pt-pl5)*(200/72));#this 200 and 72 is factor to change speed of single wheel
    pl4=average(L4);sl4=((center_pt-pl4)*(200/72));
    #print "full array", grey[scan_line_loc[4]]
    #print 'L5 pos' ,pl5, 'length',len(L5),average(lastseen),len(lastseen)
    print grey[scan_line_loc[4]]
    #print 'L4 pos',pl4 , 'lenght',len(L4)
    '''if pl5 != 999 and len(L5)<=50: #this is simple curve case sl5> mens left turn and vice versa
		if sl5>=0:
			if sl5<100:
				print "lf",100-sl5,'left slow'
			else:
				print "lb",sl5-100,'left back'
		elif sl5<0:
			if sl5>-100:
				print 'rf',100+sl5 , 'right slow'
			else:
				print 'rb',-sl5-100, 'right back'
		
    elif pl5 != 999 and len(L5)>55: # this is 90deg turn case
		if sl5>=0:
			sl5t=sl5+len(L5)
			if sl5t<100:
				print '90 deg left'
			else:
				print '90 left sharp'
		elif sl5<0:
			sl5t=sl5-len(L5)
			if sl5t>-100:
				print '90 right sharp'
			else:
				print '90 right turn'   
    




'''






















cap.release()
cv2.destroyAllWindows()
print '\n',datetime.datetime.now()


