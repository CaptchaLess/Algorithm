# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 23:15:31 2016

@author: pjh
"""

import Image
import numpy as np

def getTemplate(img_test):
    im1 = Image.open('Template1/0130')
    im2 = Image.open('Template1/3214')
    im3 = Image.open('Template1/7564')
    im4 = Image.open('Template1/7849')
    bw_im1 = im1.convert('1')
    bw_im2 = im2.convert('1')
    bw_im3 = im3.convert('1')
    bw_im4 = im4.convert('1')
    #bw_im1 = numpy.ndarray(im1)
    dic_0 = np.asarray(bw_im1.crop((0,0,10,10)))
    dic_1 = np.asarray(bw_im1.crop((10,0,20,10)))
    dic_2 = np.array(bw_im2.crop((10,0,20,10)))
    dic_3 = np.array(bw_im2.crop((0,0,10,10)))
    dic_4 = np.array(bw_im2.crop((30,0,40,10)))
    dic_5 = np.array(bw_im3.crop((10,0,20,10)))
    dic_6 = np.array(bw_im3.crop((20,0,30,10)))
    dic_7 = np.array(bw_im3.crop((0,0,10,10)))
    dic_8 = np.array(bw_im4.crop((10,0,20,10)))
    dic_9 = np.array(bw_im4.crop((30,0,40,10)))
    Dict = [dic_0,dic_1,dic_2,dic_3,dic_4,dic_5,dic_6,dic_7,dic_8,dic_9]
    
    dic_0 = np.asarray(dic_0, dtype='bool')
    dic_1 = np.asarray(dic_1, dtype='bool')
    a = dic_0^dic_1
    b = [dic_0,dic_1]
    c = b[0]
    dic_2 = np.asarray(dic_2, dtype='int32')
    
    img_test = img_test.convert('1')
    for i in range(4):
        subImg = img_test.crop((i*10,0,(i+1)*10,10))
         
        
    

    
    

if __name__=="__main__":
    img_test = Image.open("test")
    getTemplate(img_test)
    #im_bw = im.convert('1')
    dic_0 = Image.open("dic_0.jpg")
    dic_0 = np.asarray(dic_0, 'int32')
    #print(im.format, im.size, im.mode)
   # box = (0,0,10,10)
    #t1 = im.crop((20,0,30,10))
    #t1.show()
    #im.show()
    #dic_0.show()