"""
akkapop prasompon
640631128
quiz 14 - quiz 16
"""

#############
## quiz 14 ##
#############

import numpy as np
from scipy.linalg import solve

A = np.array([[1,2],[3,4]])
B = np.array([1,4])
x = solve(A , B)
print(x)

#############
## quiz 15 ##
#############

M = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(M)
print(M[2,:])
print(M[2:])

"""
M[2,:] and M[2:] provided a difference result 
because M[2,:] will display all column in only row 3 
but M[2:] will display all column from row 3 up to row n(last row)
"""
#############
## quiz 16 ##
#############

m = int(input("input m : "))
n = int(input("input n : "))

a = np.zeros((m,n)) # create empty matrix

#fill empty element with value
for i in range(0,m,1):
    for j in range(0,n,1):
        if (i < j) and (j != m)  :
            a[i][j] = 0
        elif (i == j) or (j == m) :
            a[i][j] = 1
        else :
            a[i][j] = -1           

print('result : ')
print(a)
