#Docstrings

def greet (m):
    """Prints a greeting message to the user."""
    print("Hello, " + m)
    
greet("Harpal")
print(greet.__doc__) #accessing doc string inside greet 