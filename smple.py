import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

img= cv2.imread('pic1.png')

cv2.imshow('origin',img)
def one_time_filt(img):
    T1 = np.copy(img)
    T2 = np.copy(img)
    for line in img:
        for one in line:
            if one[0]>130:
                one[1] =0
                one[2] =0
                one[0] = 255
    return img

after = one_time_filt(img)
cv2.imshow('after',after)
cv2.waitKey(0)