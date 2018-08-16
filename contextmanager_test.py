#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from contextlib import contextmanager

class Query(object):
	def __init__(self,name):
		self.name = name
	def query(self):
		print("Query info about %s ..." % self.name)

@contextmanager
def create_query(name):
	print("Begin..")
	q = Query(name)
	yield q
	print("End")
		
		
if __name__ == "__main__":
	with create_query('Bob') as q:
		q.query()