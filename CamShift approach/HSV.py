import cv2
import numpy as np

def nothing(x):
    pass

cam = cv2.VideoCapture(0)

#Create Window for Trackbar
cv2.namedWindow('Trackbar')

#Create Trackbar
cv2.createTrackbar('Hmin', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('Hmax', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('Smin', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('Smax', 'Trackbar', 0, 255, nothing)
#cv2.createTrackbar('Vmin', 'Trackbar', 0, 255, nothing)
#cv2.createTrackbar('Vmax', 'Trackbar', 0, 255, nothing)

#Set Trackbar Positions
cv2.setTrackbarPos('Hmin', 'Trackbar', 0)
cv2.setTrackbarPos('Hmax', 'Trackbar', 179)
cv2.setTrackbarPos('Smin', 'Trackbar', 0)
cv2.setTrackbarPos('Smax', 'Trackbar', 255)
#cv2.setTrackbarPos('Vmin', 'Trackbar', 0)
#cv2.setTrackbarPos('Vmax', 'Trackbar', 255)

while(1):
    #Read image from camera
    ret, img = cam.read()

    #Convert from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Get Trackbar Readings
    hmin = cv2.getTrackbarPos('Hmin', 'Trackbar')
    hmax = cv2.getTrackbarPos('Hmax', 'Trackbar')
    smin = cv2.getTrackbarPos('Smin', 'Trackbar')
    smax = cv2.getTrackbarPos('Smax', 'Trackbar')
    #vmin = cv2.getTrackbarPos('Vmin', 'Trackbar')
    #vmax = cv2.getTrackbarPos('Vmax', 'Trackbar')

    #Creating arrays to store the min and max HSV ranges
    lower = np.array([hmin, smin, 0])
    upper = np.array([hmax, smax, 255])

    #Create binary mask of in range object
    mask = cv2.inRange(hsv, lower, upper)

    #Bitwise AND operation on orginal image using mask
    obj = cv2.bitwise_and(img, img, mask=mask)

    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    maxArea = 0
    maxAreaIndex = 0

    # loop over the contours
    for c in cnts:
        area = cv2.contourArea(c)
        if(area>maxArea):
            maxArea = area
            maxAreaIndex = c

        # compute the center of the contour
	M = cv2.moments(cnts[maxAreaIndex])
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

        # draw the contour and center of the shape on the image
        #cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
        #cv2.putText(img, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Object', obj)
    k = cv2.waitKey(1) & 0xff
    if(k==27):
        break

cv2.destroyAllWindows()
cam.release()
