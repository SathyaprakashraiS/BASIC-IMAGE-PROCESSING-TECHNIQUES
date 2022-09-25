# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:13:43 2022

@author: SATHYA
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
import time 

img = cv2.imread("chess.jpg")
img = cv2.GaussianBlur(img, (3,3), 0) 

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)
cv2.imwrite("prewittychess.jpg",img_prewitty)

time.sleep(5)
img = cv2.imread('prewittychess.jpg')
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*r
    y0 = b*r
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2.imwrite('linesDetectedchess.jpg', img)
