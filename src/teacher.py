#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 23:00
# @Author  : hyang
# @File    : teacher.py
# @Software: python_utils



from config.settings import path
from src.MyPickle import MyPickle
import os


class Behavior(object):
    path = ''
    def fetchobj(self, obj):
        pick = MyPickle(obj.path)
        iter_obj = pick.loaditer()
        for item in iter_obj:
            if item.name == obj.name:
                print('find obj ',item.__dict__)
                return obj
        else:
            print('obj is not exist')

    def createobj(self,obj):
        pick = MyPickle(obj.path)
        if not self.fetchobj(obj):
            pick.dump(obj)
            print('create object', obj.__dict__)
        else:
            print('object exists')

    def delobj(self,obj):
        pick = MyPickle(obj.path)
        pick.delobj(obj)
        print('del object', obj.__dict__)

    def fetchall(self,obj):
        pick = MyPickle(obj.path)
        iter_obj = pick.loaditer()
        obj_list = []
        for item in iter_obj:
            obj_list.append(item)
        return obj_list

    def printobj(self,obj):
        obj_list = self.fetchall(obj)
        for item in obj_list:
            print(item.__dict__)


class Teacher(Behavior):
    path = os.path.join(path, "teacher_obj")

    def createobj(self):
        self.name = input('teacher name >')
        self.age = input('teacher age >')
        super().createobj(self)


class Classes(Behavior):
    path = os.path.join(path, "class_obj")
    def createobj(self):
        self.name = input('class name >')
        super().createobj(self)


class School(Behavior):
    path = os.path.join(path, "school_obj")

    def createobj(self):
        self.name = input('school name >')
        self.addr = input('school addr >')
        super().createobj(self)


class Subject(Behavior):
    path = os.path.join(path, "subject_obj")

    def createobj(self):
        self.name = input('subject name >')
        super().createobj(self)

#
# t1 = Teacher()
# t1.name = 'alex'
# t1.age = 18
#
#
# t1.createTeacher()
# t2 = Teacher()
# t2.name = 'egon'
# t2.age = 18
# t2.createTeacher()
#
# t2_obj = t2.readTeacher('egon')
# print(t2_obj.__dict__)
# t2.delTeacher()
# t3_obj = t2.readTeacher('egon')
# # print(t3_obj.__dict__)
