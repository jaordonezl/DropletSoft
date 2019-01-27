# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

img = cv2.imread('img.jpg')
#retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
#cv2.imshow('original',img)
#cv2.imshow('threshold',threshold)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#retval, threshold = cv2.threshold(grayscaled, 10, 155, cv2.THRESH_BINARY)
#cv2.imshow('original',grayscaled)
#cv2.imshow('threshold',threshold)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',img)
cv2.imshow('Otsu threshold',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()