set1 = {"Harpal", 19, 89.50}
set2 = {"Om", 20, 85.50}



#union and update
# set3 = set1.union(set2)
# print(set3)

# set1.update(set2)
# print(set1)



#intersection and intersection_update
# set4 = set1.intersection(set2)
# print(set4) #no same values

# set1.intersection_update(set2)
# print(set1) #no same values



#symmetric_difference and symmetric_difference_update()
# set5 = set1.symmetric_difference(set2)
# print(set5) #all values except common ones

# set1.symmetric_difference_update(set2)
# print(set1) #all values except common ones



#difference and difference_update
# set6 = set1.difference(set2)
# print(set6) #values in set1 but not in set2

# set1.difference_update(set2)
# print(set1) #values in set1 but not in set2




#SET METHODS:
#1. isdisjoint()
print(set1.isdisjoint(set2))

#2. issuperset()
print(set1.issuperset(set2))

#3. issubset()
print(set1.issubset(set2))

#4. pop()
# set1.pop()
# print(set1)

#5. remove()
# set1.remove(19)
# print(set1)

#6. add()
# set1.add("English")
# print(set1)

#7. update()
# updateset = [3,4,5,6]
# set1.update(updateset)
# print(set1) #values in set1 and updateset

#8. clear()
# set1.clear()
# print(set1) #empties the set1

#9. del()
# del set1


