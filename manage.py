#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 22:59
# @Author  : hyang
# @File    : manage.py
# @Software: python_utils

from bin import main
from src.teacher import Teacher
from src.teacher import Classes
from src.teacher import School
from src.teacher import Subject

if __name__ == '__main__':
   main.interactive(School)
   main.interactive(Teacher)
   main.interactive(Subject)

