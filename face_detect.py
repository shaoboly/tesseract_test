import numpy as np
import cv2
import csv


_in_dir = 'F:/tesseract/tu/'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
up_casade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

img = cv2.imread(_in_dir+'test3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    #cv2.rectangle(img, (int(x*0.92), int(y*0.4)), (int((x + w)*1.2), int((y + h)*1.25)), (255, 0, 0), 2)
    xb = int(x*0.94)
    xe = int((x + w)*1.2)
    yb = int(y*0.4)
    ye = int((y + h)*1.25)
    ylen = len(img)
    xlen = len(img[0])
    for j in range(yb,ye):
        if j>=len(img):
            break
        for i in range(xb,xe):
            if i>=len(img[0]):
                break
            img[j][i] = [255,255,255]



    #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #roi_gray = gray[y:y + h, x:x + w]
    #roi_color = img[y:y + h, x:x + w]
    '''eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)'''

cv2.imshow('img',img)
#cv2.imshow('gray',gray)
cv2.waitKey(0)
