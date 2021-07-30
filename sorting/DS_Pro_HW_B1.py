## Data Science Programming
## Homework: B1
## Akkapop Prasompon
## 640631128
## Create: July 30, 2021 
## Last update: July 31, 2021 

### Creat a function ###

# Add number to the list
# Also checking for negative interger
def add_item(list):
    # for item = 0 to 3
    for item in range(0, len(list)):
        input_text = "%s - Input positive integer : " % (item+1)
        # if input is negative integer -> loop
        while list[item] < 0:
            list[item] = int(input(input_text))
            if list[item] < 0:
                print("Try again. Please input positive integer.")
    print('Your integers are : %s'% list )            
    return list

# swap function
# list: list of number (box)
# i: position n that want to swap
def bubble_swap(list,i) :
    temp = list[i+1]    
    list[i+1] = list[i] 
    list[i] = temp
    return list

# I added "extended" because this function not just checking an integer number but also check a digit
# Inspired by "extended kalman filter"
def extended_bubble_sort(list):
    for i in range(0, len(list)-1, 1):
        for j in range(0, len(list)-i-1, 1): # general bubble sort  algorithm
            # Let's breaking an element j and j+1 into multiple digit
            # for example [10],[112] to [1,0],[1,1,2]
            a = str(list[j]) # turn integer in j to string for count a digit -> let call it "a"
            b = str(list[j+1]) # turn integer in j+1 to string for count a digit -> let call it "b"
            elm_a = [] # create list to store elements in a
            elm_b = [] # create list to store elements in b
            for k in range(0, len(a),1):
                elm_a.append(a[k]) # breaking each digit of j into list
            for k in range(0, len(b),1):
                elm_b.append(b[k]) # breaking each digit of j+1 into list
            
            # Sometimes j and j+1 have the difference length
            # We want to compare it like a[0]<->b[0] , a[1]<->b[1] , ... , a[n]<->b[n]
            # To prevent an error "index out of range", I keep duplicating the last element of the shorter one until the number of length is equal to another one
            if len(a) > len(b) : 
                diff = len(a)-len(b) # find a differnce of lenge of a and b (Ex. a=[1,2,3,4], b=[1,2,3] -> dif is 4-3 = 1)
                last_b = elm_b[len(b)-1] # get the numbere of last element  (Ex. [1,2,3] -> last is 3)
                for k in range(0,diff,1):
                    elm_b.append(last_b) # add an element until length is equal to "a"
                # Condition part (Sorting)     
                for k in range(0,len(a),1): # comparing a[0]<->b[0] , a[1]<->b[1] , ... , a[n]<->b[n]
                    if elm_a[k] < elm_b[k] : # if a[x] < b[x] 
                        list = bubble_swap(list,j) # then swap j with j+1 
                        break   # and exit loop to next j
                    elif elm_a[k] > elm_b[k] : # else if a[x] > b[x] 
                        break   # then exit loop and skip to next element
            elif len(a) < len(b) :
                diff = len(b)-len(a)
                last_a = elm_a[len(a)-1]
                for k in range(0,diff,1):
                    elm_a.append(last_a)
                # Condition part (Sorting) 
                for k in range(0,len(b),1):
                    if elm_a[k] < elm_b[k] :
                        list = bubble_swap(list,j)
                        break
                    elif elm_a[k] > elm_b[k]:
                        break
            elif len(a) == len(b) : # in this case, the number of digits of "a" and "b" are equal. Hence, I don't need to add an element
                # Condition part (Sorting) 
                for k in range(0,len(a),1):
                    if elm_a[k] < elm_b[k] :
                        list = bubble_swap(list,j)
                        break
                    elif elm_a[k] > elm_b[k]:
                        break
    return list     # return result

def list_to_int(list):
    text = ""
    for i in range(0,len(list),1):
        text += str(list[i])
    return text        

### End of Function creation ###


# Create box that contain list of four positive integer
box = list([-1])*4

# Add items into the box
add_item(box)

# Calculate the highest integer        
result = extended_bubble_sort(box)
final_result = list_to_int(box)

# Display the result       
print('Com re-arranged to : ',result)        
print('Final integer : ', final_result)

