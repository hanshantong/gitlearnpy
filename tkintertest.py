#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"


from tkinter import *

import tkinter.messagebox as messagebox

class ApplicationFrame(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel = Label(self,text="Hello,thinter")
		self.helloLabel.pack()
		self.quitButton = Button(self,text="退出",command=self.quit)
		self.quitButton.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='hello',command=self.setMessage)
		self.alertButton.pack()
	
	def setMessage(self):
		name = self.nameInput.get() or 'Apple'
		messagebox.showinfo("Message",'Hello, %s' % name)
		
		
		
if __name__ == "__main__":
	app = ApplicationFrame()
	app.master.title('Hello thinter') #设置窗口标题
	app.mainloop()  #主消息循环