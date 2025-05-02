try:
    num = int(input("Enter the integer: "))
except ValueError:
    print("Number entered is not integer")
else:
    print("Integer accepted")
finally:
    print("This block will always executed")