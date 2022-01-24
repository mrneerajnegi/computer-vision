#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import cv2


# In[5]:


img_cv=cv2.imread("../Computer-Vision-with-Python/DATA/00-puppy.jpg")


# In[6]:


#it hangs in mac/linux , so we do this with script
# cv2.imshow("Puppy",img_cv)
# cv2.waitKey()


# In[7]:


while True:
    cv2.imshow("Puppy",img_cv)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()


# In[ ]:




