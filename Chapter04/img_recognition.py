import numpy as np
import argparse
import cv2

# load the image
image = cv2.imread("sample.png")

# find all the 'black' shapes in the image
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])
shapeMask = cv2.inRange(image, lower, upper)

squares=0
# find the contours in the mask
(_,cnts, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

#find number of black squares in the image
for cnt in cnts:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx)==4:
        squares=squares+1

print ("I found %d black shapes" % (len(cnts)))
print ("Additionally I found %d black squares" % squares)
cv2.imshow("Mask", shapeMask)
 
# loop over the contours
for c in cnts:
	# draw the contour and show it
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Image", image)
