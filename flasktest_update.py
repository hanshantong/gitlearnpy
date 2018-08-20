#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')
	
@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')
			  
			  

			  
			  
@app.route('/signin',methods=['POST'])			  
def signin():
	#需要从request对象读取表单内容：
	username = request.form['username']
	passwd = request.form['password']
	if username == 'admin' and passwd == 'password':
		return render_template('signin_ok.html')
	return render_template('form.html', message="Bad username or password", username=username)
	
	
	
if __name__ == "__main__"	:
	app.run()
	