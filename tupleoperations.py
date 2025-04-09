#1. Manipulating Tuples

countries = ("India", "Russia", "America", "Britain", "Nepal")
temp = list(countries)
temp.append("Shri Lanka")
print(temp)
temp.pop(5)
print(temp)



#2. Tuple Methods
print(countries.count("India"))

print(countries.index("America"))