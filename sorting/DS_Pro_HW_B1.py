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
def extended_bubble_sort(list):
    for i in range(0, len(box), 1):
        for j in range(0, len(box)-i-1, 1):
            a = str(list[j]) # get how many digit in element j -> store as a
            b = str(list[j+1]) # get how many digit in element j+1 -> store as b
            elm_a = [] # elements in a
            elm_b = [] # elements in b
            for k in range(0, len(a),1):
                elm_a.append(a[k]) # separate each digit into list
            for k in range(0, len(b),1):
                elm_b.append(b[k])   
            print("\n",a," and ", b)    
            if len(a) > len(b) :
                diff = len(a)-len(b)
                last_b = elm_b[len(b)-1]
                for k in range(0,diff,1):
                    elm_b.append(last_b)
                for k in range(0,len(a),1):
                    print("left:",elm_a[k]," | right",elm_b[k])
                    if elm_a[k] < elm_b[k] :
                        temp = list[j+1]
                        list[j+1] = list[j]
                        list[j] = temp
                        print('break')
                        print(list)
                        break
            elif len(a) < len(b) :
                diff = len(b)-len(a)
                last_a = elm_a[len(a)-1]
                for k in range(0,diff,1):
                    elm_a.append(last_a)
                for k in range(0,len(b),1):
                    print("left:",elm_a[k]," | right",elm_b[k])
                    if elm_a[k] < elm_b[k] :
                        temp = list[j+1]
                        list[j+1] = list[j]
                        list[j] = temp
                        print('break')
                        print(list)
                        break
            elif len(a) == len(b) :
                for k in range(0,len(a),1):
                    print("left:",elm_a[k]," | right",elm_b[k])
                    if elm_a[k] < elm_b[k] :
                        temp = list[j+1]
                        list[j+1] = list[j]
                        list[j] = temp
                        print('break')
                        print(list)
                        break
    return list                        
        
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
