# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:28:10 2024

@author: Student
"""

a= float(input("Nhập hệ số a: "))
b= float(input("Nhập hệ số b: "))
c= float(input("Nhập hệ số c: "))
if a+b>c:
    print("a,b,c là 3 cạnh trong tam giác")
elif a+c>b:
    print("a,b,c là 3 cạnh trong tam giác")
elif b+c>a:
    print("a,b,c là 3 cạnh trong tam giác")
else:
    print("a,b,c không phải là 3 cạnh trong tam giác")