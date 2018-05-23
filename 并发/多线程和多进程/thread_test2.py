#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/22 21:50
# @Author  : hyang
# @Site    : 
# @File    : thread_test2.py
# @Software: PyCharm

import threading
import time

# def func():
#     time.sleep(5)


# 文本数据，图片数据
# # 创建线程
# if __name__ == '__main__':
#     t = threading.Thread(target=func)
#     t.setDaemon(True)
#     t.setName('1号')
#     print(t.getName())
#     t.start()

# class My_Thread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         time.sleep(3)  # 每个子线程默认会等待3s
#         print(self.name)
#
#
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     # thread_list = []
#     for i in range(5):
#         t = My_Thread('thread%s'%i)
#         # t.setDaemon(True)
#         t.start()
#         if t.isDaemon():
#             print("the father thread and the son thread are done")
#         else:
#             print("the father thread is waiting the son thread····")
#     print(time.time() - start_time)
#     # 如果t.setDaemon(False), 主线程打印完最后一句话后，等待sonthread运行完，然后程序才结束，所以输出结果为
# """
# the father thread is waiting the son thread····
# the father thread is waiting the son thread····
# the father thread is waiting the son thread····
# the father thread is waiting the son thread····
# the father thread is waiting the son thread····
# 0.0010001659393310547
# thread1 #子线程运行
# thread0
# thread3
# thread2
# thread4
# """
# # 如果启用t.setDaemon(True) ，这段代码的运行流程是：
# # 当主线程打印完最后一句话后，不管 son thread 是否运行完，程序立即结束，所以输出结果为：
# """
# the father thread and the son thread are done
# the father thread and the son thread are done
# the father thread and the son thread are done
# the father thread and the son thread are done
# the father thread and the son thread are done
# 0.0009999275207519531
# #因为子线程运行sleep时，主线程运行完成，程序立即结束,
# 不会打印
# thread0
# thread3
# thread2……
# """
#
# t.setDaemon(True)
from threading import Thread
from multiprocessing import Process
import multiprocessing
import os

def work1():
    global n
    n=0
    print('children', multiprocessing.current_process().name,n)

def work2():
    global n
    n=0
    print('children', threading.current_thread().name,n)

if __name__ == '__main__':
    n=100
    p=Process(target=work1)
    p.start()
    p.join()
    print('主进程',n) #毫无疑问子进程p已经将自己的全局的n改成了0,但改的仅仅是它自己的,查看父进程的n仍然为100


    n=1
    t=Thread(target=work2)
    t.start()
    t.join()
    print('主线程',n) # 查看结果为0,因为同一进程内的线程之间共享进程内的数据



