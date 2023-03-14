# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

change images

"""
import cv2 as cv
import sys

file_name = 'C:/Users/taeheon/Desktop/Chap02/imgs/soccer.jpg'
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx=0.1, fy=0.1)
gray_small_2 = cv.resize(gray, dsize=(0,0), fx=0.2, fy=0.2)
gray_small_3 = cv.resize(gray, dsize=(0,0), fx=0.3, fy=0.3)
gray_small_4 = cv.resize(gray, dsize=(0,0), fx=0.4, fy=0.4)
gray_small_5 = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)
gray_small_6 = cv.resize(gray, dsize=(0,0), fx=0.6, fy=0.6)
gray_small_7 = cv.resize(gray, dsize=(0,0), fx=0.7, fy=0.7)
gray_small_8 = cv.resize(gray, dsize=(0,0), fx=0.8, fy=0.8)
gray_small_9 = cv.resize(gray, dsize=(0,0), fx=0.9, fy=0.9)
gray_small_10 = cv.resize(gray, dsize=(0,0), fx=1.0, fy=1.0)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_2)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_3)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_4)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_5)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_6)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_7)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_8)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_9)
cv.imwrite('C:/Users/taeheon/Desktop/Chap02/imgs/soccer_gray_small.jpg', gray_small_10)

    
cv.imshow('Gray Image Small', gray_small)
cv.imshow('Gray Image Small_2', gray_small_2)
cv.imshow('Gray Image Small_3', gray_small_3)
cv.imshow('Gray Image Small_4', gray_small_4)
cv.imshow('Gray Image Small_5', gray_small_5)
cv.imshow('Gray Image Small_6', gray_small_6)
cv.imshow('Gray Image Small_7', gray_small_7)
cv.imshow('Gray Image Small_8', gray_small_8)
cv.imshow('Gray Image Small_9', gray_small_9)
cv.imshow('Gray Image Small_10', gray_small_10)
    
cv.waitKey()
cv.destroyAllWindows()    
