#1.built-in
a = [12,14,1,5,1,7,1,555,5548,6547,32145,25417,124567,12]
print(min(a))
print(max(a))
print(len(a))
print(sum(a))
print(type(a))


#2.user-defined
d = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add (d,b):
    return d + b
def sub (d,b):
    return d - b
def mul (d,b):
    return d * b
def div (d,b):
    return d / b
def floor (d,b):
    pass

print(add(d,b))
print(sub(d,b))
print(mul(d,b))
print(div(d,b))
print(floor(d,b))