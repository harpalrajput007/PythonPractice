# f = open("example.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()




f = open("example.txt", "w")
lines = ["Hello, World!\n", "This is a test.\n", "Goodbye!\n"]
f.writelines(lines)
f.close()