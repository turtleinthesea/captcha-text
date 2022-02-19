{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import muggle_ocr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MuggleOCR Session [ocr] Loaded.\n",
      "验证码\n"
     ]
    }
   ],
   "source": [
    "# 初始化；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种,OCR能识别中文\n",
    "sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)\n",
    "\n",
    "with open(r\"验证码.jpg\", \"rb\") as f:\n",
    "    b = f.read()\n",
    "text = sdk.predict(image_bytes=b)\n",
    "print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MuggleOCR Session [captcha] Loaded.\n",
      "3o78\n"
     ]
    }
   ],
   "source": [
    "# ModelType.Captcha 可识别4-6位验证码\n",
    "sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)\n",
    "with open(r\"3078.jpg\", \"rb\") as f:\n",
    "    b = f.read()\n",
    "text = sdk.predict(image_bytes=b)\n",
    "print(text) # decode('utf-8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nos.path.join()\\nos.path.exists()\\nos.path.dirname()\\nos.listdir()\\n'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "os.path.join()\n",
    "os.path.exists()\n",
    "os.path.dirname()\n",
    "os.listdir()\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pytesseract\n",
    "from PIL import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "验证码\n"
     ]
    }
   ],
   "source": [
    "captcha = Image.open('验证码.jpg')\n",
    "pytesseract.pytesseract.tesseract_cmd = r'D:\\Tesseract\\tesseract.exe'\n",
    "result = pytesseract.image_to_string(captcha, lang='chi_sim') # chi_tra 百度文字识别OCR\n",
    "print(result.strip().replace(' ',''))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
