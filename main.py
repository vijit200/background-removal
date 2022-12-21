import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(cv2.CAP_PROP_FPS,60)
segment = SelfiSegmentation()
fpsreader = cvzone.FPS()
#imbg = cv2.imread(r"images\wallpapersden.com_beautiful-cool-mountains-hd_640x480.jpg")

listimg = os.listdir("images")
imglist = []
for imgpatg in listimg:
    img = cv2.imread(f"images/{imgpatg}")
    imglist.append(img)
indexofimg = 0
while True:


    success, img = cap.read()
    imgout = segment.removeBG(img,imglist[indexofimg],threshold = 0.8)
    imgstack = cvzone.stackImages([img,imgout],2,1)
    _, imgstack = fpsreader.update(imgstack,color = (0,0,255))
    
    cv2.imshow('imageout',imgstack)

    key = cv2.waitKey(1)
    if key==ord('a'):
        if indexofimg>0:
            indexofimg -=1
    if key==ord('d'):
        if indexofimg < len(imglist)-1:
            indexofimg +=1
    if key==ord('q'):
        break