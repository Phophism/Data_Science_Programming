# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:00:04 2021

@author: Akkapop Prasompon 640631128

Problem solving Ice cream shop
"""

from scipy.linalg import solve

# We have 2 equation

# (1) ->  0.5(x1) + 0.2(x2) <= 10 
# where 0.5,0.2 means  volumn of fresh milk using for make vanilla and strawberry ice cream 
# and 10 is total fresh milk per day

# (2) -> x1 + x2 <= 30 
# where 30 is number of doll per day

# x1 denoted to number of vanilla ice cream that sold per day
# x2 denoted to number of strawberry ice cream that sold per day

# I pull the constance out of equation and I got 0.5,0.2 for first equation and 1,1 for second equation
# so the matrix will look like
#   [ [0.5,0.2]
#     [  1,  1] ]

# then I create a equation for maximum profit
# (3) -> 2(x1)+3(x2)
# again I pull out 
a = [[0.5,0.2],[1,1]]
b = [[10],[30]]
x = solve(a,b)
x
