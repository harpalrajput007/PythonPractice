x = 7 # global variable

def my_function():
    y = 3 # local variable
    print(y)
    
my_function()
print(x)
# print(y)  # This will raise a NameError because y is not defined in this scope


a = 44

def my_function2():
    global a  # Declare a as global
    a = 3  # This creates a new local variable a
    y = 7
    print(a)
    
my_function2()
print(a)  # This will print the global variable a
# print(y)  # This will raise a NameError because y is not defined in this scope