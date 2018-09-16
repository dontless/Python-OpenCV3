# -*- coding: utf-8 -*-
"""
Drawing the geometry shape

Created on Sat Sep 15 19:45:09 2018

@author: Rahul kumar
"""

import cv2  #importing the opencv
import numpy as np # importing the numpy as np 
def main():             # defining the function here 
    
    
    img1=np.zeros((512,512,3),np.uint8)   # this function define some matrix of all zeros 
                                           # pass the dimention of the image with size of 3 
                                           # uint8 stand for unsigned data set of image 
    
    
    cv2.line(img1,(0,99),(99,0),(255,0,0),2) # img passing show which coordinate want to draw  and 255,0,0 shows color  and 2 shows the thickness 
    cv2.rectangle(img1,(44,60),(200,179),(0,230,0),3) # herel ets try to make the rectangle    
    cv2.circle(img1,(70,70),30,(0,0,255),-1)# here we are making the circle  and passing radius of circle as 70 ,70 and radius as -1 fill all
   
    cv2.ellipse(img1,(160,260), (50,20),0,0,60,(127,127,127),-1)      # here angle control the portion of ellips want to shown   

      # draw a complexshape called polygon
     # for  polygon we need points so, define the point first 
    points=np.array([[80,2],[125,0],[170,0],[230,5],[30,50]],np.int32) # it defines the array which is library present in the numpy
    
    points=points.reshape((-1,1,2))# we have reshape the point to shoot our perpuse 
    
    cv2.polylines(img1,[points],True,(0,255,255)) # img where we suppose to draw the stuff and let suppose array should be true  
    
    text1="Test Text"
    cv2.putText(img1,text1,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0)) ## img is image where have to write the text and the (100,100) show the area where have to write 
                  
    cv2.imshow('airplane',img1)
    cv2.waitKey(0)
    cv2.destroyWindow('airplane')
    
    
if __name__== '__main__':
   main()    
  