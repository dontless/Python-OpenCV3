# -*- coding: utf-8 -*-
"""
 matplotlib and  colormaps 

Created on Sun Sep 16 15:12:06 2018

@author: Rahul kumar
"""
import cv2
import matplotlib.pyplot as plt 

def main():
    imgpath="C:\\Users\\Rahul kumar\\Music\\image_database\\misc\\4.2.05.tiff"
    img=cv2.imread(imgpath,0)
     
    plt.imshow(img, cmap='Greys')# output of theese plt imshow is shown in the python consol and we can copy these also 
                    # it basically create object of image and it understand the color map concept which asssign color by itself 
                    # predominant in single chain 
                    #we can change the color map  i.e- cmap= grey 
                    # we can title the widow  by using plt.title(gray colormap)
    plt.title('Gray Colormap')
    plt.xticks([]) # this makes the number on axis disappear on x axis 
    
    plt.yticks([]) # this makes the number disappear on y axis 
    
    plt.show()
   
   # cv2.imshow("airplane",img)
    #cv2.waitKey(0)
   # cv2.destroyAllWindows()
    
    
if __name__== "__main__":
   main()
    
    
    
    
    


