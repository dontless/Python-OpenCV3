# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:07:32 2018

@author: Rahul kumar
"""
"""
0.to aquare image by webcam, rasberry pie,or from dataset of image in disk 
1. lets say variable name imgpath
2. there is method called cv2.imread() to read the image  
3. img store in the imgpath
4. here we name the window name lena  and  pass the paramiter img
5. this is to bind the keyboard event to the call of  cv2.imshow method
6. This will destroy the all windows

"""
import cv2

def main():
 
    imgpath="C:\\Users\\Rahul kumar\\Music\\image_database\\misc\\4.2.05.tiff"
    img=cv2.imread(imgpath) 
    cv2.imshow('Lena', img)  
    cv2.waitKey(0)    
    cv2.destroyAllWindows() 
if __name__ == "__main__":
   main()
        

