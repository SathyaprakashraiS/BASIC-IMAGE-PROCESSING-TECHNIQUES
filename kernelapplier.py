# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:48:53 2022

@author: SATHYA
"""

import cv2
import numpy
#img=cv2.imread("D:\SEM VII\VISION AND IMAGE PROCESSING\programs\gscale save.png",cv2.IMREAD_COLOR)
img=cv2.imread("D:\SEM VII\VISION AND IMAGE PROCESSING\programs\gscale save.png",0)
#cv2.imshow("tdisp",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
print(img.shape)


q=[
   [-1,0,1],
   [-2,0,2],
   [-1,0,1],
   ]

'''
q=[
   [1,2,1],
   [0,0,0],
   [-1,-2,-1],
   ]
'''
'''
q=[
   [0,1,0],
   [1,-4,1],
   [0,1,0],
   ]
'''
dims=img.shape
modded=img
height=dims[0]
width=dims[1]
print(height)
print(width)
print(img[0][735])
def applier(a,s,d,f,g,h,j,k,l,n,m):
    modded[n][m]=((a*q[0][0])+(s*q[0][1])+(d*q[0][2])+(f*q[1][0])+(g*q[1][1])+(h*q[1][2])+(j*q[2][0])+(k*q[2][1])+(l*q[2][2]))
    #modded[n][m]=int(modded[n][m]/255)
    modded[n][m]=int(modded[n][m]/9)
    #modded[n][m]=int(modded[n][m]/(q[0][0]+q[0][1]+q[0][2]+q[0][1]+q[1][1]+q[1][2]+q[2][0]+q[2][1]+q[2][2]))
    '''
    for i in range(3):
        for j in range(3):
            pass
    '''
#q=numpy.zeros([3,3],dtype=int)
    
for i in range(height):
    for j in range(width):
        if(i!=0 and i!=height-1 and j!=0 and j!=width-1):
            applier(img[i-1][j-1],img[i-1][j],img[i-1][j+1],img[i][j-1],img[i][j],img[i][j+1],img[i+1][j-1],img[i+1][j],img[i+1][j+1],i,j)
            #print(i,j)
        else:
            modded[i][j]=0
            
            '''
for i in range(3):
    for j in range(3):
        print(i,j)
        '''
cv2.imshow("tdisp",modded)
cv2.waitKey(0)
cv2.destroyAllWindows()        