#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
Student module.
'''

__author__ = 'tongzi'

class Person(object):
	__slots__ = ('name','age','title')
	def work(self):
		print("Person is working...")



class Student(Person):
	#__slots__ = ('name','age','title')
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def print_info(self):
		print("name: %s, age: %s"%(self.name,self.age))
	
	def work(self):
		print("Student is learning...")
		
		
	@property
	def gender(self):
		return self.gender
		
	@gender.setter
	def gender(self,val):
		self.gender = val
		
	def __str__(self):	
		return ("Student object-->> name: %s, age: %s"%(self.name,self.age))
	__repr__ = __str__	
		
		
		
class Teacher(Person):
	def work(self):
		print("Teacher is teaching...")

class Lawyer:
	def work(self):
		print("Lawyer is judging...")
def whowork(person):
	person.work()


class Dog:
	__slots__ = ('name','age')
	
if __name__ == "__main__":
	whowork(Person())
	whowork(Student('john',21))
	whowork(Teacher())
	whowork(Lawyer())
	s = Student('john',22)
	s.gender = "male"
	print(s.gender)
	
	d = Dog()
	d.name = 'MM'
	d.age = 2
	d.gender = 'male'
	print(d.gender)
	
	
	
	
	
	
	
	