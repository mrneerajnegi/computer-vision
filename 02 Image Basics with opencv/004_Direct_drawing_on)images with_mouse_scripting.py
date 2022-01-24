#!/usr/bin/env python
# coding: utf-8

# In[1]:


#we will test this with scripting
import matplotlib.pyplot as plt
import numpy as np
import cv2 


def mouseAction(action,x,y,flags,params):
    if action ==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_image,center=(x,y),color=(255,0,0),radius=20,thickness=-1)
    if action ==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(blank_image,center=(x,y),color=(0,255,0),radius=20,thickness=-1)



    
cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing",mouseAction)
blank_image=np.zeros(shape=(512,512,3))
while True:
    cv2.imshow("my_drawing",blank_image)
    if cv2.waitKey(1) & 0xFF==27 :
        break
    
cv2.destroyAllWindows()



# In[ ]:




