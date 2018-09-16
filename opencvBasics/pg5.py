# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:34:38 2018

@author: Rahul kumar
In this code we are going to understand the relationship between the image and numbers

first thing we are going to used is nature of the image we are going to used is -
1. As all know human are the biological entity and we are naturally goood in finding the realtionship or pattern
  HUmans = biology= pattern
2. we ever we want to percieve the real world we used actually visul ,audio ,smell touch etc a s input 
  senses = mathematical= numbers 
3. this is not the case with the computer bcz computer is the mathematical entity and they are very good at the number 
 computers = mathematical = number 
  
3. when ever you process or sort a visual data  so , see visual stuff as the pattern  and when ever you meet he person you just remeber that
person with his face and ou could easily judge with his face 
 bu t that thing is not with the computer bcz computer sees the every thing as the numbers 
 so, there is whole field like - artificial intilligence ,neural network , machine learning , face recognition 
 4. Image aare number for the computer vidos(rapid sequence of number ), sound (it also seem to number )
 
 let seee demo 
 these all value relevant to color images 
 
"""

import cv2 

def main():
     impath="C:\\Users\\Rahul kumar\\Music\\image_database\\misc\\4.2.05.tiff"
     img1=cv2.imread(impath,1) # read in the color formT AS IT IS 
     print(type(img1)) # this will print actual number format of image
     print(img1.dtype) # it represent the data type  of consituent member of ndarray 
     print(img1.shape)# going to see the shape of the image  i.e is the resolution of the image 
                            # here 512 is standered resolution and and 3 is the number of the channel is order in B G R 
      #next see number of image dimension have 
     print(img1.ndim)# ndim is the prolerty which return the number of dimention
     print(img1.size) # going to see the size of the image  i.e- 512x512x3= 786432
     
     #cv2.imshow('lena',img1)
     #cv2.waitKey(0)
     #cv2.destroyWindow('lena')
     
if __name__ == "__main__":
   main()


