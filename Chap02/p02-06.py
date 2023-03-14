# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

GUI

"""
import cv2 as cv
import sys

#file_name = './Chap02/smile_girl.jpg' # for VSCODE working directory is Chap02
file_name = 'C:/Users/taeheon/Desktop/Chap02/imgs/smile_girl.jpg' # for jupyter or ipython(spyder)
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

cv.rectangle(img, (540,120), (880,530), (0,0,255), 2)
cv.arrowedLine(img,(600,100),(400,100),(255,0,0),2)
cv.putText(img, 'laugh', (200,100), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)

cv.imshow('Draw', img)
cv.waitKey()
cv.destroyAllWindows()    
