#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from io import StringIO


if __name__ == "__main__":
	f = StringIO()
	f.write("StringIO")
	print(f.getvalue())
	
