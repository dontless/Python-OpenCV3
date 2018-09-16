# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:19:49 2018

@author: Rahul kumar
"""

import cv2
import matplotlib.pyplot as plt 

def main():
    j=0
    for filename in dir (cv2):
        if filename.startwith("COLOR"):
           J=J+1
            
    print("THERE ARE" +str((j+1))+'color conversion flags in opencv ')        
    
    
    
if __name__== '__main__':
   main()    