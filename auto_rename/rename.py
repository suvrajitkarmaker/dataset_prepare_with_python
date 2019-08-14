#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import cv2
cv2.__version__


# In[ ]:


path = 'H:\check/'
dirs = os.listdir(path)
s = 1500
for items in dirs:
    img = path + items
    img = cv2.imread(img)
    temp = cv2.resize(img,(1000,1000))
    temp = temp[0:188, 20:-24]
    cv2.imshow(str(items),temp)
    cv2.waitKey(0)
    age = input('age ')
    dis = input('dist ')
#     edu = input('Edu 1 for school, 2 for collage 3 for uni ')
#     ser = input('Serial ')
    ser = str(s)
#     print(s)
    s+=1
    r = '0_'+dis.upper() + '_' + age + '_' + '3' + '_' + ser
    
    if os.path.exists(path+'renameM/'+r+'.jpg'):
        print('Errr')
    else:          
        cv2.imwrite(path+'renameM/'+r+'.jpg', img)
        print(r)
        os.remove(path+items)
        cv2.destroyAllWindows()


# In[ ]:


# temp = temp[0:188, 20:-24]
# cv2.imshow(str(items),temp)
# cv2.waitKey(0)
# age = input('age ')
# dis = input('dist ')


# In[ ]:


# for items in dirs:
#     img = path + items
#     img = cv2.imread(img)
#     temp = cv2.resize(img,(783,848))
#     cv2.imshow('ff',temp)
#     cv2.waitKey(0)
#     r = input()
#     cv2.imwrite('31marchNEw/'+r+'.jpg', img)
    


# In[ ]:


# ! conda install -c conda-forge opencv 


# In[ ]:




