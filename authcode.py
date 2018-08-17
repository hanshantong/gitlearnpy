#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"


from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

#随机字母
def rndChar():
	return chr(random.randint(65,90))
	
def rndColor():
		return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
	
width = 60 * 6
height = 60


image = Image.new("RGB",(width,height),(255,255,255))

#创建font对象
font = ImageFont.truetype("arial.ttf",36)

#创建draw对象
draw = ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
		

#输出文字
for t in range(6):
	draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())
	
#模糊
image = image.filter(ImageFilter.BLUR)	
image.save('authcode.jpg','jpeg')



	
