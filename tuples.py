tup = (1,3,4,5,6,3,7,8,9)

#1. indexing
print(tup[0])  # prints 1
print(tup[1])  # prints 3
print(tup[2])  # prints 4
print(tup[-1]) # prints 9
print(tup[-2]) # prints 8


#2. check for items
if 1 in tup:
    print("1 is in the tuple")
else:
    print("1 is not in the tuple")
    
    
#3. range
print(tup[1:4])  # prints (3, 4, 5)
