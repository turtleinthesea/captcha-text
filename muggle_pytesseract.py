#!/usr/bin/env python
# coding: utf-8

# In[1]:


import muggle_ocr


# In[2]:


# 初始化；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种,OCR能识别中文
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)

with open(r"验证码.jpg", "rb") as f:
    b = f.read()
text = sdk.predict(image_bytes=b)
print(text)


# In[4]:


# ModelType.Captcha 可识别4-6位验证码
sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
with open(r"3078.jpg", "rb") as f:
    b = f.read()
text = sdk.predict(image_bytes=b)
print(text) # decode('utf-8')


# In[5]:


import os


# In[7]:


'''
os.path.join()
os.path.exists()
os.path.dirname()
os.listdir()
'''


# In[2]:


import pytesseract
from PIL import Image


# In[3]:


captcha = Image.open('验证码.jpg')
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
result = pytesseract.image_to_string(captcha, lang='chi_sim') # chi_tra 百度文字识别OCR
print(result.strip().replace(' ',''))


# In[ ]:




