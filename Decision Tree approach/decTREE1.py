import cv2
from matplotlib import pyplot as plt
from sklearn import svm
import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn import tree

img=cv2.imread('w1n.jpg',0)
img1=cv2.imread('w2n.jpg',0)
img2=cv2.imread('w3n.jpg',0)
img3=cv2.imread('w4n.jpg',0)
des0=np.zeros((1,32))
surf = cv2.ORB_create()

# # kp1, des1 = surf.detectAndCompute(img1,None)
# #ret1,frame1=vid.read()
# # print len(kp),des
# #print 'len',des.shape
# #k=int(len(des)*0.25)
# # print 'k',k
# cap = cv2.VideoCapture(0)
# bf = cv2.BFMatcher()

# while(True):  
# 	ret,frame=cap.read() 
# 	kp, des = surf.detectAndCompute(img,None)
# 	kp1, des1 = surf.detectAndCompute(frame,None)
# 	matches = bf.match(des,des1)
# 	matches = sorted(matches, key = lambda x:x.distance)
# 	img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
# 	img3 = cv2.drawMatches(img,kp,frame,kp1,matches[:400],None,flags=2)
# 	# plt.imshow(img3)
# 	# plt.show()
# 	if cv2.waitKey(1) & 0xFF==ord('q'):
# 		break
# cap.release()	
# cv2.destroyAllWindows()
# exit()
des_val=np.zeros((1,32))

#clf = svm.SVC(kernel='poly',degree=5,probability=True)
clf=tree.DecisionTreeClassifier()
kp, des = surf.detectAndCompute(img,None)
k=int(len(des)*0.25);
#print 'k',k
k_index=random.sample(range(0,k),k);
#print 'k_in',len(k_index)
des_val=np.vstack((des_val,des[k_index]))
#print 'des val',des_val.shape
des=np.delete(des,(k_index),axis=0)
#print 'des',qes.shape
des0=np.vstack((des0,des))
#print 'des',des0.shape
kp,des=surf.detectAndCompute(img1,None)
k=int(len(des)*0.25);
k_index=random.sample(range(0,k),k);
des_val=np.vstack((des_val,des[k_index]))
des=np.delete(des,(k_index),axis=0)
des0=np.vstack((des0,des))
kp,des=surf.detectAndCompute(img2,None)
k=int(len(des)*0.25);
k_index=random.sample(range(0,k),k);
des_val=np.vstack((des_val,des[k_index]))
des=np.delete(des,(k_index),axis=0)
des0=np.vstack((des0,des))
kp,des=surf.detectAndCompute(img3,None)
k=int(len(des)*0.25);
k_index=random.sample(range(0,k),k);
des_val=np.vstack((des_val,des[k_index]))
des=np.delete(des,(k_index),axis=0)
des0=np.vstack((des0,des))

vid=cv2.VideoCapture(0)
count=0
new_des=np.zeros((1,32))
while(vid.isOpened() and count<20):        
    ret1,frame1=vid.read()
    ngray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    kp2, des2 = surf.detectAndCompute(ngray,None)
    new_des=np.vstack((new_des,des2))
    count=count+1
vid.release()
des0 = np.delete(des0, (0), axis=0)
des_val= np.delete(des0, (0), axis=0)
new_des = np.delete(new_des, (0), axis=0)
one=np.ones((len(des0),1))
zer=np.zeros((len(new_des),1))
o=np.vstack((one,zer))
des0=np.vstack((des0,new_des))
#print des0.shape
#print des0
#print o
X_train, X_test, y_train, y_test = train_test_split(des0, o, test_size=0.20)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
#print 'accuracy',accuracy_score(y_test,y_pred)
'''
#cap=cv2.VideoCapture(0)

thresh = 0.70

    
k=KMeans(n_clusters=3)  

cnt_1=np.array([0,0,0])
ind=0

while(cap.isOpened()):      
    a1=[]
    b1=[]
    indxkm = []
    cnt=[]
    ret, frame3 = cap.read()  

    gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    kp3, des3 = surf.detectAndCompute(gray3,None) 
    try:

        out=clf.predict_proba(des3)
        #print 'out',out 
    except Exception:
        pass
    cnt.append(1)
    for i in range(len(out)):

        if out[i][1] >= thresh:   
            cnt=np.append(cnt,i)
    if len(cnt)>10:     
        for mat in range(len(cnt)):
            index = cnt[mat]
            (x1,y1) = kp3[index].pt
            a1.append(x1)
            b1.append(y1)
            x=np.c_[a1,b1]


        k.fit(x)      
        cent = k.cluster_centers_
        for i in range(len(k.labels_)): 
            cnt_1[k.labels_[i]]=cnt_1[k.labels_[i]]+1  
        lab=np.max(cnt_1)
        for i in range(len(cnt_1)):
            if lab==cnt[i]:
                ind=i


        cv2.circle(frame3, (int(cent[ind][0]),int(cent[ind][1])),50, (0, 255,0), 5)  
    else:
        pass
       
    cv2.imshow('detect',frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
frame3=cv2.imread('w1.jpg')  
#print 'frame size',frame3.shape
frame3 = cv2.resize(frame3,None,fx=0.2, fy=0.2,interpolation = cv2.INTER_CUBIC)
#gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
kp3, des3 = surf.detectAndCompute(frame3,None) 
#print len(des3)
#print des3[0]
thresh = 0.70
k=KMeans(n_clusters=3)
cnt_1=np.array([0,0,0])
ind=0
a1=[]
b1=[]
indxkm = []
cnt=[]
try:

    out=clf.predict_proba(des3)
    #print 'out',len(out) 
except Exception:
    pass
cnt.append(1)
for i in range(len(out)):

    if out[i][1] >= thresh:   
        cnt=np.append(cnt,i)
if len(cnt)>10:     
    for mat in range(len(cnt)):
        index = cnt[mat]
        (x1,y1) = kp3[index].pt
        a1.append(x1)
        b1.append(y1)
        x=np.c_[a1,b1]


    k.fit(x)      
    cent = k.cluster_centers_
    #print 'old cent',cent
    #print k.labels_
    for i in range(len(k.labels_)): 
        cnt_1[k.labels_[i]]=cnt_1[k.labels_[i]]+1  
    lab=np.max(cnt_1)
  

    for i in range(len(cnt_1)):
        if lab==cnt[i]:
            ind=i
    
    ######################################
    ## OpenCV takes the Blue channel first, green channel second and red channel third.
    ## its not RGB. Its BGR
    ## which means frame3[:,:,0] is blue channel, frame3[:,:,1] is green channel, frame3[:,:,2] is red channel.!!! 
    #####################################
    green = np.array([0,0,0])
    for i in range(len(cnt_1)):
    	#print cent
    	#cent[i]=cent[i]-50
    	#print cent[i][0]
        for x in range(int(cent[i][0]-50),int(cent[i][0]+50)):
     	  for y in range(int(cent[i][1]-50),int(cent[i][1]+50)):
		if x < 0 or x >= frame3.shape[0] or y < 0 or y >= frame3.shape[1]:     
		  continue
		else:		
		  if ((frame3[x,y,0]>30) and (frame3[x,y,0]<50) and (frame3[x,y,1]>119) and (frame3[x,y,2]<25)) :
     			green[i]=green[i]+1
    ind = np.argmax(green)
    print "#green points in cluster 0:",green[0]
    print "#green points in cluster 1:",green[1]
    print "#green points in cluster 2:",green[2]


    print "cluster with max green:",ind
    print "all cluster centers:",cent
    print "best cluster center:",cent[ind]

    cv2.circle(frame3, (int(cent[0][0]),int(cent[0][1])), 20, (255, 0,0), 5)   # Blue circle
    cv2.circle(frame3, (int(cent[1][0]),int(cent[1][1])), 20, (0, 255,0), 5)   # Green Circle
    cv2.circle(frame3, (int(cent[2][0]),int(cent[2][1])), 20, (0, 0,255), 5)   # Red circle

    if ind==0:
	print "BLUE circle is the best cluster"
    if ind==1:
	print "GREEN circle is the best cluster"
    if ind==2:
	print "RED circle is the best cluster"
     			
	    	#print 'frame orig',frame3
	    	#print 'range value',int(cent[i][0]+50),int(cent[i][0]-50)
		
			
			#print x
	    	
	    		#print 'frame3',frame3.shape
	    		
    				
else:
    pass
   
cv2.imshow('detect',frame3)
''' 
cap.release()'''
cv2.waitKey(0)
