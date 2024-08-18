# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:53:14 2024

@author: Student
"""
from math import sqrt
a= float(input("Nhập hệ số a: "))
b= float(input("Nhập hệ số b: "))
c= float(input("Nhập hệ số c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        if c==0:
            print("Phương trình có nghiệm bằng 0")
        else:
            print("Phương trình có nghiệm bằng", -c/b)
else:
    delta = b ** 2 - 4 * a * c
    if delta<0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có nghiệm kép bằng ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", (-b - sqrt(delta)) / (2 * a))
        print("x2 = ", (-b + sqrt(delta)) / (2 * a))