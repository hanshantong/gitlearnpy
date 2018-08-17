#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from PIL import Image,ImageFilter

im = Image.open("earth.jpg")
w,h = im.size
print("Original image size: %sx%s" % (w,h))

im.thumbnail((w//2,h//2))  #//表示整除
print("Resize image to %sx%s" % (w//2,h//2))
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')

im.save('thumnail.jpg','jpeg')
