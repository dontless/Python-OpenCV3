# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:24:02 2018

@author: Rahul kumar
"""

import cv2 
import numpy as np 

 
    
windowName="Drawing Demo "# name of the windows is windowName which value is Drawing Demo 
# creating img as image which have brg 
img=np.zero((512,512,3),np.uint8)
    #here creating the window here 
cv2.namedWindow(windowName)
    
    
    #true if mouse is pressed 
drawing = False 
# if the draw rectangle press  'm' to toggle to curve

mode = True  # it is going too storethe status of the mkeys of the keyboard
(ix, iy) = (-1,-1)
 
 
 #mouse callback function 
  
def draw_shape(event, x, y, flags , param): 
             #event is event 
               #x is the x co ordinate 
               #y  is  the y coordinate 
               #flags and parameter are parameter 
     
     global ix, iy , drawing ,mode # these all are the global parameter 
     
     
     if event == cv2.EVENT_LBUTTONDOWN: # if the left buttton of these thing down then it saying drawing equal to true 
         drawing = True
         (ix,iy)= x,y
         
     elif event == cv2.EVENT_MOUSEMOVE: # if the mouse move then also drawing is True 
         
         if drawing == True:
             cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
     else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
            
if event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode ==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
                cv2.setMouseCallback(windowName,draw_shape)
        
def main():
            global mode 
            while (True):
                cv2.imshow(windowName,img)
                k=cv2.waitKey(1)
                if k== ord('m') or k == ord('M'):
                    mode = not mode 
                elif k == 27:
                       break
                   
                    
            cv2.destroyAllWindows()
if __name__=="__main__":
     main()          
            
         