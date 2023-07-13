# fruits = ["apple", "banana", "orange"]
# fruits.append("grape")
# print(fruits) #["apple", "banana", "orange", "grape"]
# fruits.insert(1, "mango")
# print(fruits) #["apple", "mango", "banana", "orange", "grape"]
# fruits.remove("apple")
# print(fruits) #["mango", "banana", "orange", "grape"]
# del fruits[2]
# print(fruits) #["mango", "banana", "grape"]

# Write a Python program that asks the user to enter five numbers and stores them in a list. Then, display the numbers entered by the user.

# num_list = []

# for num in range(5):
#   list_num = int(input(f"Please enter number {num+1}: "))
#   num_list.append(list_num)

# print(num_list)

# Write a Python program that calculates the sum of all even numbers from 1 to 20 using a for loop.

# total = 0

# for num in range(1, 21):
#   total += num

# print(total)

# Write a Python function called reverse_list that takes a list as input and returns a new list with the elements in reverse order. Test the function by providing a list of numbers and printing the reversed list.

# def reverse_list(input_list):
  
#   new_list = []

#   for i in range(0, len(input_list)):
#     new_list.append(input_list[len(input_list) - 1 - i])

#   return new_list

# print(reverse_list([1, 2, 3, 4, 5]))

# Write a Python program that asks the user to enter a sentence and counts the number of words in the sentence. Assume that words are separated by spaces.

def num_words(sentence):
  num = sentence.count(" ")
  return f"There are {num + 1} words in this sentence."

entry = input("Please enter a sentence: ")
print(num_words(entry))
