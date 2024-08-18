# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:09:33 2024

@author: Student
"""

a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
if a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm bằng ", -b/a)