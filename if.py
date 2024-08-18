# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 06:53:24 2024

@author: Student
"""

diem=float(input("Nhập điểm trung bình (GPA) của bạn: "))
diem=input()
if diem >=3.5 and diem <5:
    print("Học lực Yếu")
elif diem >=5 and diem <7:
    print("Học lực Trung Bình")
elif diem >=7 and diem <8:
    print("Học lực Khá")
elif diem >=8 and diem <9:
    print("Học lực Giỏi")
elif diem >=9 and diem <=10:
    print("Học lực Xuất Sắc")
else:
    print("Học lực Kém")