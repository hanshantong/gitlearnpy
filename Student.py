#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
Student module.
'''

__author__ = 'tongzi'

from enum import Enum

class Person(object):
	#__slots__ = ('name','age','title')
	def work(self):
		print("Person is working...")



class Student(Person):
	#__slots__ = ('name','age','title')
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self._gender = gender
		
	def print_info(self):
		print("name: %s, age: %s"%(self.name,self.age))
	
	def work(self):
		print("Student is learning...")
		
		
	@property
	def gender(self):
		return self._gender
		
	@gender.setter
	def gender(self,val):
		self._gender = val
		
	def __str__(self):	
		return ("Student object-->> name: %s, age: %s, gender: %s"%(self.name,self.age,self._gender))
	__repr__ = __str__	
	
	def __getattr__(self, attr):
		if attr == "score":
			return 100
		return None
	def __call__(self):
		print("Student->> name is %s, age is %s"%(self.name,self.age))
	
def student2dict(s):
	return {'name':s.name,'age':s.age,'gender':s._gender}
	
def dict2student(d):
	return Student(d['name'],d['age'],d['gender'])

	
		
class Teacher(Person):
	def __init__(self,name,age,title):
		self.name = name
		self.age = age
		self.title = title

	def work(self):
		print("Teacher is teaching...")

class Lawyer:
	def work(self):
		print("Lawyer is judging...")
def whowork(person):
	person.work()


class Dog:
	__slots__ = ('name','age',"gender")



Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

	
if __name__ == "__main__":
	import json
	whowork(Person())
	#whowork(Student('john',21))
	#whowork(Teacher())
	whowork(Lawyer())
	s = Student('john',22,'male')
	s.gender = "male"
	print(s.gender)
	
	d = Dog()
	d.name = 'MM'
	d.age = 2
	d.gender = 'male'
	print(d.gender)
	print(s.score)
	print(json.dumps(s,default=student2dict))
	t = Teacher("Lee",35,'Professor')
	print(json.dumps(t,default=lambda obj:obj.__dict__))
	json_str = '{"name": "john", "age": 22, "gender": "male"}'
	print(json.loads(json_str,object_hook=dict2student))
	
	
	
	
	
	
	