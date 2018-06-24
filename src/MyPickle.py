#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 17:30
# @Author  : hyang
# @File    : MyPickle.py
# @Software: luffy_test

import pickle
import os


class MyPickle(object):
    def __init__(self,file_name):
        self.file_name = file_name

    def dump(self,obj):
        with open(self.file_name,'ab') as f:
            pickle.dump(obj,f)

    def loaditer(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'rb') as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        yield obj
                    except:
                        break

    def edit(self,obj):  # 编辑，修改
        f2 = MyPickle(self.file_name+'.old')
        for item in self.loaditer():
            if item.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(item)
        os.remove(self.file_name)
        os.rename(self.file_name+'.old',self.file_name)


    def delobj(self, obj):
        f2 = MyPickle(self.file_name + '.old')
        for item in self.loaditer():
            if item.name != obj.name:
                f2.dump(item)
            else:
                print('del name',obj.name)
        os.remove(self.file_name)
        os.rename(self.file_name + '.old', self.file_name)