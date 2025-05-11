#seek()
# with open("example.txt", "r") as file:
#     # Move the cursor to the 5th byte
#     file.seek(5)
#     # Read the next 10 bytes
#     data = file.read(10)
#     print(data)  # Output: 'is a te'



#tell()
# with open("example.txt", "r") as file:
#     data = file.read(10)
    
#     current_position = file.tell()
    
#     print(f"Current position: {current_position}")  # Output: Current position: 10



#truncate()
with open("sample.txt", "r+") as file:
    file.write("Hello world!")  # Write to the file
    file.truncate(5)  # Truncate the file to the first 10 bytes
    
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)  # Output: 'This is a'