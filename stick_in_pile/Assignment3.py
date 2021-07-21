## Data Science Programing
## Assignment 2
## Akkapop Prasompon
## 640631128

from random import * # random library

##### Original Setup from assignment 1 ######

stick = 0  # pile
name = ""  # user
is_player_turn = 1 # if 1 then player turn

print('---------------------------')
print('take x stick from pile')
print('---------------------------')

while stick < 1:
    stick = int(input('How many stick in the pile : '))     # input stick(s)
    if stick < 1:                                          # input less than 1 - try again
        print('Invalid Number. Try Again.')

if stick > 1:
    print('There are', stick, 'sticks in the pile.')  # there are
else:
    print('There is', stick, 'stick in the pile.')  # there is

# if (stick+2)%3==0 :
#     print("OMAE WA MOU SHINDEIRU") ## You are already dead (whatever you do, you loss)

print()  # \n

name = input('What is yor name : ')  # input name

ask = '\n' + name + ', how many stick you will take (1 or 2): '

while stick != 0:  # Game start
    
    # Player's turn
    if is_player_turn == 1:
        take = int(input(ask))
        if take > 2:  # take more than 2 sticks - No
            print('No! you cannot take more than 2 sticks!')
        elif take < 1:  # or take less than 1 stick - No
            print('No! you cannot take more less than 1 stick!')
        # or take more than remaining - No
        elif (stick - take) < 0:
            print('There are no enough sticks to take.')
        elif stick == take: # take last - end
            stick = stick-take
            print(name,'take the last stick')
            is_player_turn = 0 # No error condition : swap to smart computer turn
        else: # take 1 or 2 - count
            stick = stick-take
            if stick > 1:
                print('There are', stick, 'sticks in the pile.')  # there are
            elif stick == 1:
                print('There is', stick, 'stick in the pile.')  # there is
            is_player_turn = 0          # No error condition : swap to smart computer turn
    # end if
    
    # Computer's turn
    else:
        # from the fomular above
        if ((stick+2) % 3 == 0) and stick != 1:  # Always loss. So take whatever
            # random
            take = randint(1, 2)
            stick = stick - take 
            print("\nSmart Computer take :", take ,"\nThere are", stick, "sticks in the pile.")
        elif ((stick+1) % 3 == 0):  # take one to win
            # take 1
            stick -= 1
            print("\nSmart Computer take : 1\nThere are", stick, "sticks in the pile.")
        elif (stick % 3 == 0): # take two to win
            # take 2
            stick -= 2
            print("\nSmart Computer take : 2\nThere are", stick, "sticks in the pile.")
        elif stick == 1: # only 1 stick left
            stick -= 1
            print("\nSmart Computer take : 1")
        is_player_turn = 1
    # end else

if is_player_turn == 1:
    print('\nCongratulation! You Win!\n')
else:
    print('\nSmart Computer, Win!!\n')

#####################################################################

### Explanation how I got a smart computer's stick taking fomular ###

# At first I consider the fact (that can make player win this game)

## Facts ##
# Rule#1 : Player who start with 3 sticks ALWAYS WIN
# Rule#2 : Player who start with 4 sticks ALWAyS LOSS
# Rule#3 : From Rule#1 and Rule#2, player who start with 5 , 6 sticks can determine the winner (determine whether who would start with 4 sticks)
# Principle : Do whatever you can to make opponent start with 7 , (or 10)

# I try to follow the rules that I have set
# So I decided to start using these rules after there are 12 sticks left in the pile
# Then I created a Psudocode
# let say
    # IF stick > 12 :
    #   random
    # ELSE IF stick == 12:
    #   take 2
    # ELSE IF stick == 11:
    #   take 1
    # ELSE IF stick == 10 :
    #   random
    # ELSE IF stick == 9 :
    #   take 2
    # ELSE IF stick == 8 :
    #   take 1
    # ELSE IF stick == 7 :
    #   random
    # ELSE IF stick == 6 :
    #   take 2
    # ELSE IF stick == 5 :
    #   take 1
    # ELSE IF stick == 4 :
    #   random
    # ELSE IF stick == 3 :
    #   take 2
    # ELSE IF stick == 2 :
    #   take 1
    # ELSE IF stick == 1 :
    #   take 1
# And I can notice the pattern like 1,2,random,1,2,random,...,1,2,random and so on
# So that I rewrite it to
    # IF (stick+2) % 3 == 0
    #   random
    # #ELSE IF (stick+1) %3 == 0
    #   take 1
    # ELSE IF stick % 3 == 0
    #   take 2
    
# Which mean
# if the remaining stick % 3 == 0 ---> take 2
# if the remaining (stick+1) % 3 == 0 ---> take 1
# if the remaining (stick+2) % 3 == 0 ---> You loss | take random  (or 1 in case you have to pick the last stick)
    
# And here we go, we got a smart computer.
