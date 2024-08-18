# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:21:42 2024

@author: Student
"""

x= float(input("Nhập quảng đường đã đi (km): "))
if x<=1:   
  print("Phí taxi của bạn là (ngàn đồng): ", 20*x)
elif x>1 and x<=3:
    print("Phí taxi của bạn là (ngàn đồng): ", 13*x)
elif x>=4 and x<=8:
    print("Phí taxi của bạn là (ngàn đồng): ", 3*13+12*(x-3))
else:  
    fee= 3*13+5*12+10*(x-8)
    if fee>100:
        print("Phí taxi của bạn là (ngàn đồng): ",fee*0.92)
    else:
        print("Phí taxi của bạn là (ngàn đồng): ", 3*13+5*12+10*(x-8))