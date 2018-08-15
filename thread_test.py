#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

import os


if __name__ == "__main__":
	print("Process %s start.."%os.getpid())
	pid = os.fork()
	if 0 == pid:
		print("I am a child process %s and my parent is %s"%(os.getpid(),os.getpid()))
	else:
		print("I %s just created a child process %s"%(os.getpid(),pid))