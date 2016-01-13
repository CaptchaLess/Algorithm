# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:57:58 2016

@author: Junfu Pu, pjh@mail.ustc.edu.cn

Algorithm for CaptchaLess
"""



import Image
import numpy as np

def getTemplate_yjs():
    im1 = Image.open('Template1/0130')
    im2 = Image.open('Template1/3214')
    im3 = Image.open('Template1/7564')
    im4 = Image.open('Template1/7849')
    bw_im1 = np.array(im1.convert('L'))>128
    bw_im2 = np.array(im2.convert('L'))>128
    bw_im3 = np.array(im3.convert('L'))>128
    bw_im4 = np.array(im4.convert('L'))>128
    
    dic_0 = bw_im1[:,0:10].copy()
    dic_1 = bw_im1[:,10:20].copy()
    dic_2 = bw_im2[:,10:20].copy()
    dic_3 = bw_im2[:,0:10].copy()
    dic_4 = bw_im2[:,30:40].copy()
    dic_5 = bw_im3[:,10:20].copy()
    dic_6 = bw_im3[:,20:30].copy()
    dic_7 = bw_im3[:,0:10].copy()
    dic_8 = bw_im4[:,10:20].copy()
    dic_9 = bw_im4[:,30:40].copy() 
    Dict = [dic_0,dic_1,dic_2,dic_3,dic_4,dic_5,dic_6,dic_7,dic_8,dic_9]
    return Dict

def makePrediction_yjs(img_test):
    Dict = getTemplate_yjs()
    dist = np.zeros((10,4))
    img_test = np.array(img_test.convert('L'))>128
    for i in range(4):
        subImg = img_test[:,i*10:(i+1)*10]
        j = 0
        for dic in Dict:
            dist[j,i] = (dic^subImg).sum()
            j += 1   
    result = dist.argmin(axis=0)
    checkcode = repr(result)
    return checkcode

def getTemplate_mis():
    Names_num = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg', \
                '7.jpg','8.jpg','9.jpg']
    Names_alp = []
    for i in range(65,91):
        Names_alp.append(chr(i)+'.jpg')
    Names_alp.remove('I.jpg')
    Dict = []
    label = []
    
    i = 1
    for name in Names_num:
        img = Image.open('Template_mis/'+name)
        bw_img = np.array(img.convert('L'))>128
        Dict.append(bw_img)
        label.append(str(i))
        i += 1
    
    for i in range(65,91):
        label.append(chr(i))
    label.remove('I')
    
    for name in Names_alp:
        img = Image.open('Template_mis/'+name)
        bw_img = np.array(img.convert('L'))>128
        Dict.append(bw_img)    
    return (Dict,label)
 
def makePrediction_mis(img_test):
    (Dict,label) = getTemplate_mis()
    dist = np.zeros((10,4))
    img_test = np.array(img_test.convert("L"))>128
    
    for i in range(4):
        subImage = img_test[i]
        j = 0
        for dict in Dict:
            d = np.zeros(10)
            for k in range(10):
                subTemplate = dict[20*k:20*(k+1),:]
                d[k] = (subTemplate^subImage).sum()
            dist[j,i] = d.min()
            j += 1
    
    result = dist.argmin(axis=0)
    checkcode = repr(result)
    return checkcode
   
    
    
if __name__=="__main__":
    img_test = Image.open("test1")
    checkcode = makePrediction_yjs(img_test)
    print(checkcode)
    getTemplate_mis()
    