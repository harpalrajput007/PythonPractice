#1.while
count = 5
while count > 0:
    print(count)
    count -= 1
    
    
#2.while-else
a = 10
while a > 0:
    print(a)
    a -= 1
else:
    print("a is negative")


#3.do-while
while True:
    user_input = int(input("Enter a positive number: "))
    if user_input < 0: #if not user_input > 0:
        break               #break