#1.break
for i in range(1,101,2):
    print(i,end = " ")
    if i == 50:
        break
    else:
        print("Ohhhh Shittt this loop is of odd numbers how can we find 50 here!")
print("Thank You!")

for i in ["harpal","darshan","om","yash","karan"]:
    print(i,end = " ")
    if i == "karan":
        break
    else:
        print("ki jai ho")
print("Bhamare")

#2.continue
for i in [2,3,4,5,6,7,8,0]:
    if i % 2 != 0:
        continue
    print(i)