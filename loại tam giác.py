# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:43:29 2024

@author: Student
"""

a= float(input("Nhập cạnh a: "))
b= float(input("Nhập cạnh b: "))
c= float(input("Nhập cạnh c: "))
if a+b>c or a+c>b or b+c>a:
  if a==b and b==c:
      print("a,b,c là 3 cạnh của tam giác đều")
  elif a==b or a==c or b==c:
      print("a,b,c là 3 cạnh của tam giác cân")
  elif a**2+b**2==c**2 or a**2+c**2==b**2 or a**2==b**2+c**2:
      print("a,b,c là 3 cạnh trong tam giác vuông")
  else:
      print("a,b,c là 3 cạnh trong tam giác thường")
else:
    print("a,b,c không phải là 3 cạnh trong tam giác")