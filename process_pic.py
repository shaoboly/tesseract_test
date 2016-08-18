#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def equalizeHist():
    pass

def two_value_pro(dir):
    x = 120
    y = 255
    pic_name = str(dir).split('/')[-1].split('.')[0]
    img = cv2.imread(dir)
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(GrayImage, x, y, cv2.THRESH_BINARY)
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    cv2.imwrite('tmp/'+pic_name+'.png',thresh1,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return 0

def fazjo_compute(img):
    maxi = np.max(img)
    mini = np.min(img)
    pre_t = (maxi+mini)/2
    while(True):
        img_f = np.copy(img)
        img_b = np