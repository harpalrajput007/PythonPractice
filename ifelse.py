#1.if-else
a = int(input("Enter your age: "))
if a >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
    
    

#2.elif
b = int(input("Enter the number: "))
if b < 0 :
    print("Number is negative")
elif b == 0:
    print("Number is zero")
else:
    print("Number is positive")



#3.nested-if
c = int(input("Enter the number: "))
if c < 0 :
    print("Number is negative")
elif c > 0 :
    if c <= 10 :
        print("Number is between 0 and 10")
    elif c <= 20 :
        print("Number is between 11 and 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")