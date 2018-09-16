# -*- coding: utf-8 -*-
"""
mini project : OpenCv BGR Pallette with trackbars 

Created on Sat Sep 15 20:41:31 2018

@author: Rahul kumar
"""

# import the needed libraries 
import cv2
import numpy as np
def main():
    #define the empty function 
    def emptyFunction():
        pass
    
    
    
    # define the empty image 
    
    img1= np.zeros((512,512,3),np.uint8)
    #create the widndow image 
    windowName='openCV BGR Color Palette'
    
    #lets create the windows 
    
    cv2.namedWindow(windowName)
    #lets create the track bar 
    
    cv2.createTrackbar('B', windowName,0,255,emptyFunction) #here createTrackbar is function. we need to blue thing for the track bar and we need to 
                                               # 0 which represent the starting position  and then pass functon to move the sliter of track bar and all 6 
    
    cv2.createTrackbar('G', windowName,0,255,emptyFunction)
                       # color :G
                       #windowName=> it is the name whic his associated with the windows 
                       #0 is the minimum values associated with the trackbar 
                       #255 is the maximum values of the range 
                       #emptyFunction it is the function it is suppose t call when we move the slider 
    cv2.createTrackbar('R', windowName,0,255,emptyFunction)
    

                                     
    while(True):
        
        cv2.imshow(windowName,img1)
        
        if cv2.waitKey(1) == 27:     # here the 27 is used as scape sequence character 
            break                    #it break when we have scape sequence 
        #fetch the parameter accordingly 
        blue= cv2.getTrackbarPos('B',windowName)
        green=cv2.getTrackbarPos('G',windowName)
        red= cv2.getTrackbarPos('R',windowName)        
        cv2.destroyAllWindows()    # destroy all windows 
        #creat composite image
        img1[:]=[blue,green,red]
        
        
if __name__ == "__main__":
    main()
    
    
