# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

read and display images

"""
import cv2 as cv
import sys

file_name = 'C:/Users/taeheon/Desktop/Chap02/imgs/soccer01.jpg'
file_name_2 = 'C:/Users/taeheon/Desktop/Chap02/imgs/soccer02.jpg'

img = cv.imread(file_name)
img_2 = cv.imread(file_name_2)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))



if img_2 is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name_2))
    

cv.imshow('Image Disply', img_2)
cv.imshow('Image Disply_2', img)
    
cv.waitKey()
cv.destroyAllWindows()    
