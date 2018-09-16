# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:38:20 2018
@author: Rahul kumar
how to read in defferent mode of color and save the output at specific path 
In this program we are going to see how to save various images first 
mode 1 is default mode -1 is alpha mode  and 0 for the grayscale 
while reading the image we can mention it as 0 or convert it grayscale 
"""
import cv2

def main():
    
    imgpath="C:\\Users\\Rahul kumar\\Music\\image_database\\misc\\4.2.05.tiff"
    
    img=cv2.imread(imgpath,0)
    
    #lets declare the postion for the saving the output to particular position
    
    Outpath="C:\\Users\\Rahul kumar\\Music\\image_database\\Output\\4.2.05.jpg"
    
    
    cv2.imshow("airoplane",img)
     
    
    #method used to save file called cv2.imwrite(path of the folder to save )
    
    cv2.imwrite(Outpath, img)
    
    cv2.waitKey(0)
    
    cv2.destroyWindow('airoplane')
    
if __name__=="__main__":
    
   main()    

