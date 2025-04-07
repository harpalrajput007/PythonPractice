# we can take input from user using input() function
# input() function returns a string

#no need of typecasting
a = input("Enter your name : ")
print("Hello, " + a + "!")


#need of typecasting
b = int(input("Enter first number : "))
c = int(input("Enter second number : "))
print("Sum of two numbers is : ",b + c)

#if didn't typecasted
f = (input("Enter first number : ")) #2
g = (input("Enter first number : ")) #3
print("Sum of two numbers is : ",f + g)  # output : 23

