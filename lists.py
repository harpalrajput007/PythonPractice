#1.list
li1 = [1,2,3,4,5,6,"Harpal","Apple"]
print(li1)


#2.list index
print(li1[0])
print(li1[1])
print(li1[6])
print(li1[7])


#3.accessing list items
#positive indexing
print(li1[0])
print(li1[1])
print(li1[2])
print(li1[3])

#negative indexing
print(li1[-1])
print(li1[-2])


#4.Checking item in list
if "Harpal" in li1:
    print("Harpal is present")
else:
    print("Harpal is absent")
    
    
    
#5. Range of index
#printing elements within a particular range
print(li1[1:4])

#printing all elements from a given index till end
print(li1[3:])

#from start to given index
print(li1[:4])

#printing alternative values
print(li1[::2])

#reversing list
print(li1[::-1])




#6. list comprehension
names = ["Harpal","Darshan","Om","Karan"]
nameswith_a = [item for item in names if "a" in item]
print(nameswith_a)

lst = [i for i in range(10) if i%2 == 0]
print(lst)