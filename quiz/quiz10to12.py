# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 2021

@author: akkapop prasompon

"""

"""

********************************************************************
quiz 10
1) create f(x) function
2) call function at the main program
check f(2.3) == 0 ?
"""

# create function 
def funct(x):
    return ((x**x)+(0.25*x)+5)

# use function
x1 = float(input("input a number : ")) #input 2.3

# apply function
result1 = funct(x1)

# show thำ result
print(result1)

# check if input number equal to 0 or not
if (result1 == 0):
    print('The result is equal to 0 !!')
else :
    print('The result is not 0')
    

"""
********************************************************************
quiz 11
Make half adder circuit
return sum and carry
"""

# create half adder function
def half_adder(x,y):
    s = int(x ^ y) # sum of binary number || x XOR y =  xy` + x`y
    c = int(x and y) # 1+1=0 with carry 1 (ทดหนึ่ง)
    # adding int() to prevent the function to return TRUE or FALSE
    return [s,c] ;    # return array including sum and carry
    
x = int(input("input first binary : ")) 

y = int(input("input second binary : "))

result2 = half_adder(x, y)

print("Sum : ", result2[0]) #print sum
print("Carry : ", result2[1]) #print carry

"""
********************************************************************
quiz 12
make full adder circuit
return sum and carry
require half_adder function from quiz 11
"""

# full adder is two half adder with carry
# so the function will be like
def full_adder(x,y,z): # z = carry
    half1 = half_adder(x, y) # operate 1st half adder
    s1 = half1[0] # sum of 1st half_adder
    c1 = half1[1] # carry of 1st half_adder
    
    half2 = half_adder(s1,z) # operate 2nd half adder by using sum of 1st half adder and z (carry) 
    s = half2[0]  # final result of sum
    c2 = half2[1] # carry of 2nd half_adder
    
    c = c1 or c2 # final result of carry
    
    return [s,c] # return result of full adder which include array of sum and carry


x = int(input("input first binary : ")) 

y = int(input("input second binary : "))

z = int(input("input third binary : "))

result3 = full_adder(x, y, z)

print("Sum : ", result3[0]) #print sum
print("Carry : ", result3[1]) #print carry
    