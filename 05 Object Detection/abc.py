#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


nadia=cv2.imread("../Computer-Vision-with-Python/DATA/Nadia_Murad.jpg",0)
denis=cv2.imread("../Computer-Vision-with-Python/DATA/Denis_Mukwege.jpg",0)
solvia=cv2.imread("../Computer-Vision-with-Python/DATA/solvay_conference.jpg",0)


# In[3]:


#plt.imshow(nadia,"gray")


# In[4]:


faceCarcade=cv2.CascadeClassifier("../Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml")


# In[5]:


#def detectImage(image):
#    image=image.copy()
#    faceRects=faceCarcade.detectMultiScale(nadia)
#    for (x,y,w,h) in faceRects:
#        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),10)
#    return image
#


# In[6]:


#plt.figure(figsize=(20,10))
#plt.subplot(1,3,1)
#plt.imshow(detectImage(nadia),"gray")
#plt.subplot(1,3,2)
#plt.imshow(detectImage(denis),"gray")
#plt.subplot(1,3,3)
#plt.imshow(detectImage(solvia),"gray")
#plt.show()


# In[7]:


def detectImage(image):
    image_c=image.copy()
    faceRects=faceCarcade.detectMultiScale(image_c,1.59,3)
    for (x,y,w,h) in faceRects:
        cv2.rectangle(image_c,(x,y),(x+w,y+h),(255,0,0),10)
    return image_c
    


# In[8]:


#plt.figure(figsize=(20,10))
#plt.subplot(1,3,1)
#plt.imshow(detectImage(nadia),"gray")
#plt.subplot(1,3,2)
#plt.imshow(detectImage(denis),"gray")
#plt.subplot(1,3,3)
#plt.imshow(detectImage(solvia),"gray")
#plt.show()


# In[9]:


eyeCarcade=cv2.CascadeClassifier("../Computer-Vision-with-Python/DATA/haarcascades/haarcascade_eye.xml")
def detectEyes(image):
    image=image.copy()
    faceRects=eyeCarcade.detectMultiScale(image)
    for (x,y,w,h) in faceRects:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),10)
    return image
    


# In[10]:


#plt.figure(figsize=(20,10))
#plt.subplot(1,3,1)
#plt.imshow(detectEyes(nadia),"gray")
#plt.subplot(1,3,2)
#plt.imshow(detectEyes(denis),"gray")
#plt.subplot(1,3,3)
#plt.imshow(detectEyes(solvia),"gray")
#plt.show()


# In[ ]:


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    face=detectImage(frame)
    cv2.imshow('frame',face)
    if cv2.waitKey(1) & 0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:




