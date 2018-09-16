# -*- coding: utf-8 -*-
"""
colorspaces  in opencv 
Created on Sun Sep 16 15:40:00 2018

@author: Rahul kumar
"""
import cv2
import matplotlib.pyplot as plt 

def main():
    
    imgpath ="C:\\Users\\Rahul kumar\\Music\\image_database\\misc\\4.2.05.tiff"
    img=cv2.imread(imgpath,1)# it is stie in memory as bgr  
    img1 =cv2.cvtColor(img,cv2.COLOR_BGRA2RGB) # IT IS THE C color visible to the human eyes and human brain 
    
    
    plt.imshow(img) # it dispaly by default image in rgb format 
    
    plt.title("colr image with BGR")
    
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    
    plt.imshow(img1) # it dispaly by default image in rgb format 
    
    plt.title("colr image with default colormap")
    
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
if __name__=="__main__":
    main()

