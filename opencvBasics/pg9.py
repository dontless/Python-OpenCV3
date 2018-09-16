# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:22:08 2018

@author: Rahul kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:38:21 2018

@author: Rahul kumar
"""

#import the required librearies 

import cv2
import numpy as np

#create a black image and a windows 
windowName="Drawing " # define the name of the window i.e- Drawing

#define the image of 512 by 512 of resolution 
#it gonna be color image bcz we want to have more color 
img=np.zeros((512,512,3),np.uint8)

#creating the windowName variable with windowName which is Drawing 

cv2.namedWindow(windowName)

#Mouse callbackfunction 
def draw_circle(event,x,y,flags,param):  
               #event is event 
               #x is the x co ordinate 
               #y  is  the y coordinate 
               
    if event == cv2.EVENT_FLAG_LBUTTON:  #here we are checking if the event lbutton  double click i.e event of mouse 
        #when there is double click it is goiing to draw the circle by fetching he coordinate of x,y
        
        cv2.circle(img,(x,y),40,(0,255,0),-1) #cicle is drawn on img which have coordinate  of center is x,y and the radius is 40 
                                               #and the color is green 
                                               #ging to occupy the hole cicle with the color 
                                               
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,0,255),-1)
        
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),20,(0,0,255),-1)
    if event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img,(x,y),20,(0,0,255),-1)
# bind the callback function to windows
cv2.setMouseCallback(windowName,draw_circle)  #going to associate the custome write function which is draw_circle assign to windoNmae drawing 

        
def main():
    
   while(True):
       cv2.imshow(windowName,img)
       if cv2.waitKey(20) == 27: #  pressig the scape sequence going to destroy the window 
           break
       
           cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()    