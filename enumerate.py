a = ["apple", "banana", "cherry"]
for index, value in enumerate(a):
    print(index, value)
    
a1 = ["apple", "banana", "cherry"]
for index, value in enumerate(a, start=1):
    print(index, value)
    
b = ("apple", "banana", "cherry")
for index, value in enumerate(b):
    print(index, value)
    
b1 = ("apple", "banana", "cherry")
for index, value in enumerate(b):
    print(f"{index+1} : {value}")
    
c = "Harpal"
for index, value in enumerate(c):
    print(index, value)