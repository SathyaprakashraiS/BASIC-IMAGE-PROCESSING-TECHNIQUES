# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:15:44 2022

@author: SATHYA
"""
#https://github.com/JAGALINGAM/vision-and-image-processing
#using MATLAB
'''
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
 
img = mpimg.imread('tst0.jpg')
#img = mpimg.imread('tst1.png')
#img = mpimg.imread('tst2.png')
plt.imshow(img)
'''


#using PIL
from PIL import Image

img = Image.open('tst0.jpg')
img.show()
print(img.format)
print(img.mode)
#to save image in any other formats
#im1 = img.save("testing.png")
im1 = img.convert('L')
#img.save('greyscale.png')
im1 = im1.save("gscale save.png")



'''
#using OPEN CV
import cv2
img = cv2.imread('tst0.jpg')
cv2.imshow('padam :)', img)
cv2.waitKey(0)       
cv2.destroyAllWindows()
'''
