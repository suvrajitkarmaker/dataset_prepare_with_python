#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pyautogui
import time


# In[156]:


pyautogui.position()


# In[161]:


for po in range(1,100,1):
    if(po==1):
        pyautogui.click(235,96)#1stpositionclick and open picture
        pyautogui.click(235,96)
    else:
        pyautogui.press('down')
        pyautogui.press('enter')
    time.sleep(2)
    for i in range(1,4,1):#percent _change_in_paintApp
        time.sleep(1)
        pyautogui.click(1464,846)
    time.sleep(2)
    pyautogui.click(132,106)#click_for_crop
    time.sleep(2)
    pyautogui.click(132,224)#click_for_crop
    pyautogui.hotkey('ctrl', 'shift', 'x')
    pyautogui.moveTo(305, 152,duration=1)
    pyautogui.dragTo(6, 577, 1,button='left')
    pyautogui.hotkey('ctrl', 'shift', 'x')
    pyautogui.click(39,15)#click_for_save
    pyautogui.click(39,15)#click_for_save
    pyautogui.click(1577,5)#click_for_exit
    time.sleep(2)


# In[157]:





# In[ ]:
