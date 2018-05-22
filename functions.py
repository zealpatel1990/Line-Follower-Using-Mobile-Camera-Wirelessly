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
    thresold = average(array)/2;L=[]#here thresold is not set
    for j in range(0,len(array)):
            if array[j]<thresold:
                append(oL,j,L)
    if len(L)==0: 
		L.append(999); 
		if oL[0]!=999: global lastseen; lastseen=oL;###point to be noted line is not found
    return L

def get_white_line_array(array,oL):
    thresold = average(array)*2;L=[]
    for j in range(0,len(array)):
            if array[j]>thresold:
                append(oL,j,L)
    if len(L)==0: L.append(999)###point to be noted line is not found
    return L
