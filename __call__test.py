#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)

		
if __name__ == "__main__":
	p = Person('yin jia ying','male')
	print(p('Ole Lee'))