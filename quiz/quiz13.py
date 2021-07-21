# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21, 2021

Quiz 13

akkapop prasompon
640631128

"""

L = [1,2]
L3 = 3*L

"""
1. what is content of L3
Answer: List of 3 times of L
    = [L,L,L]
    = [1,2,1,2,1,2]
"""

"""
2. Try to predict the outcome of the following commands
L3[0] 
L3[-1]
L3[10]

Answer:
    L3[0] : First element of L3 which is 1
    L3[-1] : Last element of L3 which is 2
    L3[10] : Return "error out of range" due to the length of L3 is 6 
"""

"""
3. What does the following command do?

L4 = [k**2 for k in L3]

Answer: k represent each item in L3
        For each item in L3 will be power by 2 and add to variable L4
        So, L4 will be
        = [1**2,2**2,1**2,2**2,1**2,2**2]
        = [1,4,1,4,1,4]
    
"""

"""
4. Concatenate L3 and L4 to a new list L5
"""
L4 = [k**2 for k in L3]

L5 = L3+L4
L5
