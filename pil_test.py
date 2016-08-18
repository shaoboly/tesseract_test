#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

_in_dir = 'F:/tesseract/tu/'

x= 240
y = 255

img = cv2.imread(_in_dir+'test3.jpg')


GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh1=cv2.threshold(GrayImage,x,y,cv2.THRESH_BINARY)

cv2.imshow("thresh1", thresh1);

contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow('test',img)



'''kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))

closed = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
# 显示腐蚀后的图像
cv2.imshow("Close", closed);

# 开运算
opened = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
# 显示腐蚀后的图像
cv2.imshow("Open", opened)'''
print np.average(thresh1)

th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                    cv2.THRESH_BINARY,3,5)
'''ret,thresh2=cv2.threshold(GrayImage,x,y,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(GrayImage,x,y,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(GrayImage,x,y,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(GrayImage,x,y,cv2.THRESH_TOZERO_INV)
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])'''

#plt.imshow(thresh1,'gray')
#plt.show()
cv2.waitKey(0)

