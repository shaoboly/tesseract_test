#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
from  process_pic import *

_in_dir = 'F:/tesseract/tu/'

x= 120
y = 255

img = cv2.imread(_in_dir+'test7.jpg')
cv2.imshow('test0',img)
#img = color_filt1(img)

#cv2.imshow('test1',img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2, 2))
'''
eroded = cv2.erode(img,kernel)
#显示腐蚀后的图像
cv2.imshow("Eroded Image",eroded)

dilated = cv2.dilate(eroded,kernel)
cv2.imshow('dilute',dilated)'''


GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh1=cv2.threshold(GrayImage,x,y,cv2.THRESH_BINARY)

cv2.imshow("thresh1", thresh1);

GrayImage = cv2.GaussianBlur(GrayImage,(3,3),0)

edges = cv2.Canny(GrayImage,50,100)

cv2.imshow('ed',edges)

lines = cv2.HoughLines(edges,1,np.pi/360,100)

result = np.zeros_like(edges)

for line in lines[0]:
    rho = line[0] #第一个元素是距离rho
    theta= line[1] #第二个元素是角度theta
    print rho
    print theta
    if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线
                #该直线与第一行的交点
        pt1 = (int(rho/np.cos(theta)),0)
        #该直线与最后一行的焦点
        pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),result.shape[0])
        #绘制一条白线
        cv2.line( result, pt1, pt2, (255))
    else: #水平直线
        # 该直线与第一列的交点
        pt1 = (0,int(rho/np.sin(theta)))
        #该直线与最后一列的交点
        pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))
        #绘制一条直线
        cv2.line(result, pt1, pt2, (255), 2)

cv2.imshow('result',result)

'''contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow('test',img)'''



'''kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))

closed = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
# 显示腐蚀后的图像
cv2.imshow("Close", closed);

# 开运算
opened = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
# 显示腐蚀后的图像
cv2.imshow("Open", opened)'''
#print np.average(thresh1)

#th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
 #                   cv2.THRESH_BINARY,3,5)
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

cv2.destroyAllWindows()