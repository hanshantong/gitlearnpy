#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'tongzi'

import logging
import pdb

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
	s = '0'
	n = int(s)
	logging.info("n = %s"%n)
	pdb.set_trace()
	print(10 / n)