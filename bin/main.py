#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 23:03
# @Author  : hyang
# @File    : main.py
# @Software: python_utils



from src.teacher import Teacher

def interactive(object):
    menu = """
      ------- {obj}管理 ---------
      1.  创建{obj}(功能已实现)
      2.  查看{obj}(功能已实现)
      3.  删除{obj}(功能已实现)
      4.  查看{obj}列表
      5.  退出
      """ .format(obj=object.__name__)  # 获得类名

    menu_dic = {
        '1': 'createobj',
        '2': 'fetchobj',
        '3': 'delobj',
        '4': 'printobj'
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            obj = object()
            if obj.fetchall(obj):
                print('last create obj', obj.fetchall(obj)[-1].__dict__)  # 打印上次创建对象
            if user_option == '2' or user_option == '3':
                obj.name = input('input {obj} name >'.format(obj=object.__name__))
                getattr(obj, menu_dic.get(user_option))(obj)  # 反射调用对象的方法
            elif user_option == '1':
                getattr(obj, menu_dic.get(user_option))()
            elif user_option == '4':
                print('{0:*^30}'.format(object.__name__ + ' List'))
                getattr(obj, menu_dic.get(user_option))(obj)
            else:
                print('EXIT')
                exit_flag = True

        else:
            print("Option does not exist!", "error")
            exit_flag = True


if __name__ == '__main__':
    interactive(Teacher)



