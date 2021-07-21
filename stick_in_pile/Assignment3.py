# Data Science Programing
# Assignment 3
# Akkapop Prasompon
# 640631128
# 21/07/2021

from random import *  # random library

# Set the number of stick in the pile
def setStick():
    stick = 0  # declare variable
    # Keep input stick until stick > 0 
    while stick < 1: 
        # input stick(s)
        stick = int(input('How many stick in the pile : '))
        if stick < 1:                                        # check if number of stick not less than 1
            print('Invalid Number. Try Again.')
    # return value of stick's number
    return stick

# Set the name of player
def setName():
    name = input('What is yor name : ')  
    return name

# Set the maximum number of stick that player can take in each turn
def setMaxTake():
    max = 0
    while max < 1:
        max = int(input("Set maximum stick per turn : "))     # input number
        if max < 1:                                           # check if the input number not less than 1
            print('Invalid Number. Try Again.')
    # return value
    return max

# Player taking a stick out of pile, also check the condition of input
def takeStick(stick, max):
    ask = '\n' + name + ', how many stick you will take (1 to ' + str(max) + ') : '     # set menu text
    take = 0    #declare variable
    # Take the stick. If invalid value, repeat
    while (take < 1) or ((stick - take) < 0):
        take = int(input(ask))
        if take > max:  # take more than maximum number 
            print('No! you cannot take more than', max, 'sticks!')
            take = 0 # invalid, back to input
        elif take < 1:  # take less than 1 stick - No
            print('No! you cannot take more less than 1 stick!')
            take = 0 # invalid back to input
        elif (stick - take) < 0:  # not enough stick to take
            print('Not enough sticks to take. Please try again.')
            take = 0 # invalid back to input
        else:
            return take # return number of stick that has been taken

# Calculate remaining stick
def stickCal(stick, take):
    if stick == take:  # take the last stick -> end
        stick = stick-take
        if is_player_turn == 0 :
            print('Smart Computer take the last stick')
        else:      
            print(name, 'take the last stick')
        return 0
    else:  # take stick
        stick_left = stick-take
        if ((stick-take) > 1):
            print('There are', stick_left , 'sticks in the pile.')  # > 1 stick left
        elif ((stick-take) == 1):
            print('There is', stick_left , 'stick in the pile.')  # 1 stick left
        return stick_left

# Smart Computer take stick from the pile 
# Using equation (stick+i) % (max+1) = 0 where i = 0,1,...,max
# # 1 -> if number of stick equal to (stick+max) % (max+1) = 0 then player who start first will has higher chance to loss 
# # 2 -> if number of stick equal to (stick+i) % (max+1) = 0 then i is the number of stick computer should take
# # player who start with [equation 2\ can manipulate the opponent to start with [equation 1] which lead them to loss 
# # (max - i) is the number of stick that computer will take for manipulate opponent to start with [equation 1] 
def comTurn(stick,max) :
    if stick == 1:  # last stick left, must take 1
        return 1
    # Calculating
    for i in range(0,max+1,1): # i = [0,1,...,max] 
        if i != max :
            if ((stick+i) % (max+1) == 0):
                take = max-i
                print("\nSmart Computer take :", take )
                return take
        elif i == max : # player who start with i = max has a chance to loss 
            take = randint(1, max) 
            print("\nSmart Computer take :", take )
            return take
                
# Declare variable
name = setName()        # set player name
stick = setStick()      # set number of stick in the pile
max = setMaxTake()      # set maximum stick taking per turn
is_player_turn = 1      # set player to start first (if 1 then player's turn else smart computer's turn)
print()                 # new line

# Display number of stick
if stick > 1:
    print('There are', stick, 'sticks in the pile.')
else:
    print('There is', stick, 'stick in the pile.')

# Display maximum number of stick player can take per turn
print('Player can\'t take more than', max,'stick(s) per turn') 

# Game start. Loop will continue until the remaining stick = 0
while stick != 0:  
    # Player's turn
    if is_player_turn == 1:
        take = takeStick(stick, max)          # input number of stick player want to take
        stick = stickCal(stick, take)         # Calculate the remainig stick
        is_player_turn = 0                    # Switch to smart computer turn
    # Computer's turn
    else:
        take = comTurn(stick,max)             # Smart computer stick taking algorithm
        stick = stickCal(stick,take)          # Calculate the remainig stick
        is_player_turn = 1                    # Switch to player turn

# End game
if is_player_turn == 1:
    print('\nCongratulation! You Win!\n')   # Player win
else:
    print('\nSmart Computer, Win!!\n')      # Com win
