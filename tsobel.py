# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 00:57:03 2022

@author: SATHYA
"""

import cv2
import numpy
import math
img=cv2.imread("D:\SEM VII\VISION AND IMAGE PROCESSING\programs\gscale save.png",0)
#img=cv2.imread("D:\SEM VII\VISION AND IMAGE PROCESSING\programs\sudoku.jpg",0)
#cv2.imshow("tdisp",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
print(img.shape)

q=[
   [-1,0,1],
   [-2,0,2],
   [-1,0,1],
   ]
w=[
   [-1,-2,-1],
   [0,0,0],
   [1,2,1],
   ]
dims=img.shape
height=dims[0]
width=dims[1]
print(height)
print(width)
print(img[0][735])
threshold=150
max=0
min=65536
modded=numpy.zeros((height,width))
ximg=numpy.zeros((height,width))
yimg=numpy.zeros((height,width))

for i in range(height):
    for j in range(width):
        if(max<img[i][j]):
            max=img[i][j]
        if(min>img[i][j]):
            min=img[i][j]
print("MAX",max,"MIN",min)
def applier(a,s,d,f,g,h,j,k,l,n,m):
    gx=((a*q[0][0])+(s*q[0][1])+(d*q[0][2])+(f*q[1][0])+(g*q[1][1])+(h*q[1][2])+(j*q[2][0])+(k*q[2][1])+(l*q[2][2]))
    #gx=int(gx/9)
    #modded[n][m]=int(modded[n][m]/255)
    #gx=int(gx/(q[0][0]+q[0][1]+q[0][2]+q[0][1]+q[1][1]+q[1][2]+q[2][0]+q[2][1]+q[2][2]))
    gy=((a*w[0][0])+(s*w[0][1])+(d*w[0][2])+(f*w[1][0])+(g*w[1][1])+(h*w[1][2])+(j*w[2][0])+(k*w[2][1])+(l*w[2][2]))
    #gy=int(gy/9)
   
    if(gx>255):
        gx=255
    elif(gx<0):
        gx=0
    elif(gy>255):
        gy=255
    elif(gy<0):
        gy=0
       
    #gy=int(gy/(w[0][0]+w[0][1]+w[0][2]+w[0][1]+w[1][1]+w[1][2]+w[2][0]+w[2][1]+w[2][2]))
    g=int(math.sqrt((gx*gx)+(gy*gy)))
   
    if(g>255):
        g=255
    elif(g<0):
        g=0
      
    #print("G",g,"GX",gx,"GY",gy)
    
    #modded[n][m]=g
    #ximg[n][m]=gx
    #yimg[n][m]=gy
    return g,gx,gy
    
for i in range(height):
    for j in range(width):
        if(i!=0 and i!=height-1 and j!=0 and j!=width-1):
            modded[i][j],ximg[i][j],yimg[i][j]=applier(img[i-1][j-1],img[i-1][j],img[i-1][j+1],img[i][j-1],img[i][j],img[i][j+1],img[i+1][j-1],img[i+1][j],img[i+1][j+1],i,j)
            #applier(img[i-1][j-1],img[i-1][j],img[i-1][j+1],img[i][j-1],img[i][j],img[i][j+1],img[i+1][j-1],img[i+1][j],img[i+1][j+1],i,j)
            #print("recG",modded[i][j],"recGX",ximg[i][j],"recGY",yimg[i][j])
            #print(i,j)
        else:
            modded[i][j]=0
            ximg[i][j]=0
            yimg[i][j]=0
            
same=0
notsame=0
for i in range(height):
    for j in range(width):
        if(ximg[i][j]==yimg[i][j]):
            same+=1
        else:
            notsame+=1
print(same,"S NS",notsame)

cv2.imshow("SOBEL EDGE DETECTION",modded)
cv2.imshow("VERTICAL EDGE DETECTION",ximg)
cv2.imshow("HORIZONTAL EDGE DETECTION",yimg)
cv2.waitKey(0)
cv2.destroyAllWindows()