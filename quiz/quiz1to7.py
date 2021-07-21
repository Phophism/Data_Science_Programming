# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:04:29 2021

@author: akkapop
"""
count = 0
first = int(input("Please input first number : "))
second = int(input("Please input second number : "))

if first <= second :
  x = first
else:
  x = second  

while (first%x != 0 and second%x != 0):
  x = x-1
  count += 1

print("The greatest common divisor is ",x)
print(count)
