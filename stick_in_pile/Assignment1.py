stick = 0 # pile
name = "" # user
count = 0 # number of time taking stick

print('---------------------------')
print('take x stick from pile')
print('---------------------------')

while stick < 1 :
    stick = int(input('How many stick in the pile : '))     # input stick(s)
    if stick < 1 :                                          # input less than 1 - try again
        print('Invalid Number. Try Again.')
        
if stick > 1 :
    print('There are ', stick, ' sticks in the pile.') # there are
else :
    print('There is ', stick, ' stick in the pile.') # there is 
    
print() # \n
        
name = input('What is yor name : ') # input name

ask = '\n' + name + ', how many stick you will take (1 or 2): '

while stick != 0 :                                          # take until no stick left
    take = int(input(ask))
    if take > 2 :                                                   # take more than 2 sticks - No
        print('No! you cannot take more than 2 sticks!')
    elif take < 1 :                                                 # or take less than 1 stick - No
        print('No! you cannot take more less than 1 stick!')
    elif (stick - take) < 0 :                                       # or take more than remaining - No
        print('There are no enough sticks to take.')
    elif stick == take :                                            # take last - end
        stick = stick-take
        count = count+1
    else :                                                          # take 1 or 2 - count
        stick = stick-take    
        count = count + 1    
        if stick > 1 :
            print('There are',stick,'sticks in the pile.') # there are
        elif stick == 1 :
            print('There is',stick,'stick in the pile.') # there is
    
if count > 1:
    print('\nOK. There is no stick left in the pile. You spent ',count,' times. \n') # times  
else :
    print('\nOK. There is no stick left in the pile. You spent ',count,' time. \n') # time