fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits) #["apple", "banana", "orange", "grape"]
fruits.insert(1, "mango")
print(fruits) #["apple", "mango", "banana", "orange", "grape"]
fruits.remove("apple")
print(fruits) #["mango", "banana", "orange", "grape"]
del fruits[2]
print(fruits) #["mango", "banana", "grape"]
