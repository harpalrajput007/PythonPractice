# salary = int(input("Enter the salary: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Salary is not in the range of 2000 to 5000")


# Step 1: Define custom exception class
class WeakPasswordError(Exception):
    """Raised when the password is too weak"""
    pass

# Step 2: Function that checks password strength
def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Password too short! Must be at least 8 characters.")
    elif password.isnumeric():
        raise WeakPasswordError("Password too weak! Must contain letters too.")
    else:
        print("Password is strong enough.")

# Step 3: Use try-except to handle it
try:
    user_password = input("Enter your password: ")
    check_password(user_password)
except WeakPasswordError as e:
    print("WeakPasswordError:", e)
