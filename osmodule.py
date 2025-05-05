import os

# # Open file in read-only mode
# fd = os.open('example.txt', os.O_RDONLY)

# # Read up to 100 bytes
# content = os.read(fd, 100)
# print(content.decode())  # decode from bytes to string

# # Always close the file descriptor
# os.close(fd)




# # # Open file in write mode
# fd = os.open('example.txt', os.O_WRONLY)

# # # Write a string to the file
# os.write(fd, b'Hello, World!')

# # # Always close the file descriptor
# os.close(fd)y




#get a list of the files in the current directory
files = os.listdir(".")
print(files)