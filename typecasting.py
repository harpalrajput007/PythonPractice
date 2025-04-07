#typecasting 

a = "45"
b = 5

# print(a + b) will return error because a is string and b is int and we cant concatenate them.

#to convert data type of a into int we will use typecasting
print(int(a) + b)  # Output: 50
c = int(a)

print(type(a))
print(type(c))

d = 345
e = str(d)
print(e)
print(type(e))  # Output: <class 'str'>

r = float(1)
print(r)  # Output: 1.0

''' 
int()
str()
float()
complex()
ord()
hex()
oct()
tuple()
set()
list()
dict()
'''

#there are two types of typecasting 1.explicit typecasting : done by developers or programmers for there convenience and 2.implicit typecasting : done by python interpreter