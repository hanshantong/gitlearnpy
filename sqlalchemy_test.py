#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = "tongzi"

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

class Student(Base):
	__tablename__ = 'student' #表名
	
	#表的结构
	id = Column(String(20),primary_key=True)
	name = Column(String(30))
	age = Column(String(3))
	
	def __str__(self):
		return "id: " + self.id + ", name: " + self.name + ", age: " + self.age
	

#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:2015201315@localhost:3306/test')	

#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建session对象
session = DBSession()

#创建Student对象
s = Student(id='2015201315',name='Alice',age='18')
session.add(s)   #添加到sess
session.commit()   #提交即保存到数据库
session.close()    #关闭session

session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
std = session.query(Student).filter(Student.id=='2015201315').one()

print('type:',type(std))
print(std)

	
	

