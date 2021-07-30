# Add number to the list
# Also checking for negative interger

# Create box that contain list of four positive integer
box = list([-1])*4

# for item = 0 to 3
for item in range(0, len(box)):
    input_text = "%s - Input positive integer : " % (item+1)
    # if input is negative integer -> loop
    while box[item] < 0:
        box[item] = int(input(input_text))
        if box[item] < 0:
            print("Try again. Please input positive integer.")

print(box)

# swap function
# list: list of number (box)
# i: position n that want to swap
def swap(list,i) :
    temp = list[i+1]    
    list[i+1] = list[i] # then swap j
    list[i] = temp      # with j+1 
    return list

def extended_bubble_sort(list):
    for i in range(0, len(box), 1):
        for j in range(0, len(box)-i-1, 1):
            # Breaking element j and element j+1 into single digit
            # for example [10],[112] to [1,0],[1,1,2]
            a = str(list[j]) # turn integer in j to string for count a digit -> let call it "a"
            b = str(list[j+1]) # turn integer in j+1 to string for count a digit -> let call it "b"
            elm_a = [] # create list to store elements in a
            elm_b = [] # create list to store elements in b
            for k in range(0, len(a),1):
                elm_a.append(a[k]) # breaking each digit of j into list
            for k in range(0, len(b),1):
                elm_b.append(b[k]) # breaking each digit of j+1 into list
            
            # Sometimes j and j+1 having difference length
            # To prevent an error "index out of range"
            # I keep duplicating the last element of the shorter one until the number of length is equal to another element
            if len(a) > len(b) :
                diff = len(a)-len(b)
                last_b = elm_b[len(b)-1]
                for k in range(0,diff,1):
                    elm_b.append(last_b) # add an element until length is equal to "a"
                # Condition part (Sorting)     
                for k in range(0,len(a),1): # comparing a[0]<->b[0] , a[1]<->b[1] , ... , a[n]<->b[n]
                    if elm_a[k] < elm_b[k] : # if a[x] < b[x]  
                        temp = list[j+1]    
                        list[j+1] = list[j] # then swap j
                        list[j] = temp      # with j+1
                        break   # and exit loop to next j
            elif len(a) < len(b) :
                diff = len(b)-len(a)
                last_a = elm_a[len(a)-1]
                for k in range(0,diff,1):
                    elm_a.append(last_a)
                # Condition part (Sorting) 
                for k in range(0,len(b),1):
                    if elm_a[k] < elm_b[k] :
                        temp = list[j+1]
                        list[j+1] = list[j]
                        list[j] = temp
                        break
            elif len(a) == len(b) : # this case number of digits of "a" and "b" are equal. Hence, I don't need to add an element
                # Condition part (Sorting) 
                for k in range(0,len(a),1):
                    if elm_a[k] < elm_b[k] :
                        temp = list[j+1]
                        list[j+1] = list[j]
                        list[j] = temp
                        break
    return list     # return result
        
result = extended_bubble_sort(box)       
print(result)        


# Bubble Sort
    # In sorting condition
    # If having same digit Then check()
    # Else
        # Extract into multiple one-digit integers (Ex. [112] -> [1,1,2])
        # check() from left to right
         # Ex. [10],[112]
         # list_a[1,0] , list_b[1,1,2]
         # list_a[0] <-> list_b[0]  ===  1 <-> 1 ===> equal
         # if still equal
         # list_a[1] <-> list_b[1] === 0 <-> 1 ===> more than
         # then swap()
         # if list_a[0] = list_b[0] and list_a[1] <-> list_b[1]
         # list_a doesn't has list_a[2] then use list_a[1] <-> list_b[2]

# display result
