# Problem 1:
# Write a Python program that asks the user for their name and greets them with a personalized message.

# name = input("Enter your name: ")
# print(f"Hello, {name}! Nice to meet you.")

# Problem 2:
# Write a Python program that calculates the area of a rectangle. The program should ask the user for the length and width of the rectangle and then display the calculated area.

# length = input("Enter the length of the rectangle: ")
# width = input("Enter the width of the rectangle: ")
# print(f"The area of the rectangle is: {int(length) * int(width)}") 

# Problem 3:
# Write a Python program that converts temperature from Celsius to Fahrenheit. The program should ask the user for the temperature in Celsius and then display the equivalent temperature in Fahrenheit.

# celsius = input("Enter the temperature in Celsius: ")
# fahrenheit = (int(celsius) * 9/5) + 32
# print(f"The temperature in Fahrenheit is: {fahrenheit}")

# Problem 4:
# Write a Python program that calculates the total cost of a meal, including tax and tip. The program should ask the user for the cost of the meal and the tip percentage, and then calculate and display the total cost.

# meal = input("Enter the cost of the meal: ")
# tip = input("Enter the tip percentage: ")
# total = round(float(meal) * (1 + int(tip)/100), 2)
# print(f"The total cost of the meal is: {total}")

# Problem 5:
# Write a Python program that swaps the values of two variables. The program should ask the user for two numbers and then swap their values. After swapping, display the new values of the variables.

# first = input("Enter the first number: ")
# second = input("Enter the second number: ")
# print(f"""After swapping:
# First number: {second}
# Second number: {first}""")

# Problem 6:
# Write a Python program that asks the user for a number and determines whether it is even or odd. Display an appropriate message based on the input.

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#   print(f"The number {number} is even.")
# else: 
#   print(f"The number {number} is odd.")

# Problem 7:
# Write a Python program that calculates the sum of the digits in a given integer. The program should ask the user for an integer and then display the sum of its digits.

# integer = input("Enter an integer: ")
# sum = 0
# for number in integer: 
#   sum += int(number)
# print(f"The sum of the digits is: {sum}")

# Problem 8: 
# Write a Python program that calculates the factorial of a given number. The program should ask the user for a positive integer and then display its factorial.

# integer = int(input("Enter a positive integer: "))
# factorial = 1
# for i in range(1, integer + 1):
#   factorial *= i
# print(f"The factorial of {integer} is {factorial}")

# Problem 9: 
# Write a Python program that checks whether a given year is a leap year or not. The program should ask the user for a year and then display an appropriate message.

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#   print(f"The year {year} is a leap year.")
# else:
#   print(f"The year {year} is not a leap year.")

# Problem 10: 
# Write a Python program that converts a given sentence into title case. The program should ask the user for a sentence and then convert it to title case where the first letter of each word is capitalized.

# sentence = input("Enter a sentence: ")
# split_sentence = sentence.split(" ")
# print(split_sentence)

# new_split_sentence = []

# for word in split_sentence:
#   new_word = word[0].upper() + word[1:]
#   new_split_sentence.append(new_word)

# converted_sentence = " ".join(new_split_sentence)

# print(f"Converted sentence: {converted_sentence}")
