#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def equalizeHist():
    pass

def readimg(dir):
    img = cv2.imread(dir)
    return img

def face_detect(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    #up_casade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (int(x*0.92), int(y*0.4)), (int((x + w)*1.2), int((y + h)*1.25)), (255, 0, 0), 2)
        xb = int(x * 0.94)
        xe = int((x + w) * 1.2)
        yb = int(y * 0.4)
        ye = int((y + h) * 1.25)
        ylen = len(img)
        xlen = len(img[0])
        for j in range(yb, ye):
            if j >= len(img):
                break
            for i in range(xb, xe):
                if i >= len(img[0]):
                    break
                img[j][i] = [255, 255, 255]

    return img

def arg_blue(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    arg = 0.0
    count  =0
    min = 255
    for i in range(0,len(img)):
        for j in range(0,len(img)):
            one = img[i][j]
            hone = imgHsv[i][j]
            if hone[2]>80 and hone[2]<150 and one[0]>90:
                if hone[2]<min:
                    min = hone[2]
                arg+=hone[2]
                count+=1

    return min,arg/count

def color_filt(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for line in imgHsv:
        for one in line:
            if one[0]>90 and one[0]<150 and one[2]>70 and one[1]>70:
                one[1] =0
                one[2] =255
    return cv2.cvtColor(imgHsv, cv2.COLOR_HSV2BGR)

def color_filt1(img):
    for line in img:
        for one in line:
            if one[0]>110:
                one[1] =255
                one[2] =255
                one[0] = 255
    return img

def color_filt3(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(0,len(img)):
        for j in range(0,len(img)):
            one = img[i][j]
            hone = imgHsv[i][j]
            if hone[2]>90 and hone[1]>100 and hone[2]>100:
                one[1] =255
                one[2] =255
                one[0] = 255
    return img

def color_filt2(img,arg):

    for line in img:
        for one in line:
            if one[0]>arg:
                one[1] =255
                one[2] =255
                one[0] = 255
    return img

def erode_test(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    eroded = cv2.erode(img, kernel)
    return eroded

def two_value_pro(img,pic_name):
    x = 114
    y = 255
    #pic_name = str(dir).split('/')[-1].split('.')[0]
    #img = cv2.imread(dir)

    #img = color_filt(img)
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(GrayImage, x, y, cv2.THRESH_BINARY)
    thresh1 = erode_test(thresh1)
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