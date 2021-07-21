## Data Science Programing
## Assignment 3
## Akkapop Prasompon
## 640631128
## 21/07/2021

# Set number of stick in the pile
def setStick() : 
    stick = 0 # declare variable
    
    # Input stick 
    while stick < 1:
        stick = int(input('How many stick in the pile : '))     # input stick(s)
        if stick < 1:                                           # check if number of stick not less than 1
            print('Invalid Number. Try Again.')             
            
    # Display number of stick        
    if stick > 1:
        print('There are', stick, 'sticks in the pile.')    
    else:
        print('There is', stick, 'stick in the pile.')    
         
    # return value of stick's number     
    return stick

def setName() :
    name = input('What is yor name : ')  # input name
    return name

# Set number of maximum number of stick that player can take per one turn
def setMaxTake(): 
    max = 0 
    while max < 1:
        max = int(input("Set maximum stick per turn : "))     # input number
        if max < 1:                                           # check if the input number not less than 1
            print('Invalid Number. Try Again.')             
            
    # Display maximum number of stick player can take per turn        
    print('Player can\'t take more than',max,'stick(s) per turn')    
         
    # return value 
    return max
      

def takeStick(max) :
    ask = '\n' + name + ', how many stick you will take (1 or 2): '     # set menu text
    take = 0
    while take < 1 :
        take = int(input(ask))
        if take > max:  # take more than 2 sticks - No
            print('No! you cannot take more than',max,'sticks!')
            take = 0
        elif take < 1:  # or take less than 1 stick - No
            print('No! you cannot take more less than 1 stick!')
            take = 0
        else:        
            return take
    
# Player take stick    
def stickCal(stick,take) :
    if (stick - take) < 0:
        print('There are no enough sticks to take.')
        return stick
    elif stick == take: # take last - end
        stick = stick-take
        print(name,'take the last stick') 
        return 0
    else :     
        stick_left = stick-take
        if stick > 1:
            print('There are', stick, 'sticks in the pile.')  # > 1 stick left
        elif stick == 1:
            print('There is', stick, 'stick in the pile.')  # 1 stick left
        return stick_left

# Declare variable
name = setName()        # set player name
stick = setStick()      # set number of stick in the pile
max = setMaxTake()      # set maximum stick taking per turn
is_player_turn = 1      # set player to start first (if 1 then player's turn else smart computer's turn)

while stick != 0:  # Game start
    # Player's turn
    if is_player_turn == 1:
        take = takeStick()
        # or take more than remaining - No
        if (stick - take) < 0:
            print('There are no enough sticks to take.')
        elif stick == take: # take last - end
            stick = stick-take
            print(name,'take the last stick')
            is_player_turn = 0 # No error condition : swap to smart computer turn
        else: # take 1 or 2 
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
