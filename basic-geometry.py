# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:15:12 2020

@author: VRAJ PATEL
"""

import cv2
#import numpy as np

img = cv2.imread('vraj01.jpg', -1)

img = cv2.line(img, (265,265), (375,375), (83,54,132), 5)
img = cv2.arrowedLine(img, (0,0), (255,255), (83,54,132), 5) ## give the color channel in reverse
img = cv2.rectangle(img, (300,300), (540,500), (10,25,45), 1)  ##-1 is opaque
img = cv2.circle (img, (223,25), 23, (0, 213, 54), -1)   ###

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (200,12,200), 10, cv2.LINE_AA)





cv2.imshow('image01', img)

cv2.waitKey(0)
cv2.destroyAllWindows()