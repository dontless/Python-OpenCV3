# -*- coding: utf-8 -*-
"""

Mouse event and InteractiveDrawing 

Created on Sat Sep 15 21:30:08 2018

@author: Rahul kumar
"""

#import required libraries 
import cv2

 
def main():
    events =[i for i in dir (cv2) if 'EVENT' in i] 
    print(events) # print all the event present in the opencv 
     
if __name__=="__main__":
   main()     