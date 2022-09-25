# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:13:43 2022

@author: SATHYA
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
import time
img = cv2.imread("tcrcle.jpg",0)
img = cv2.GaussianBlur(img, (3,3), 0) 

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)
output = img_prewitty.copy()

cv2.imwrite("prewitty.jpg",img_prewitty)

time.sleep(5)

import cv2
import numpy as np
img = cv2.imread('prewitty.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
output = img.copy()

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imwrite('detected circles.jpg',cimg)