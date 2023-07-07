# Problem 1:
# Write a Python program that checks whether a given number is positive, negative, or zero. The program should ask the user for a number and then display an appropriate message.

# number = int(input("Please write an integer: "))
# if number > 0:
#   print("The number is positive.")
# elif number < 0: 
#   print("The number is negative.")
# else:
#   print("The number is zero.")

# Problem 2: 
# Write a Python program that checks whether a given year is a leap year or not. The program should ask the user for a year and then display an appropriate message.

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#   print(f"The year {year} is a leap year.")
# else:
#   print(f"The year {year} is not a leap year.")

# Problem 3:
# Write a Python program that calculates the maximum of three given numbers. The program should ask the user for three numbers and then display the maximum value.

# first_num = int(input("Please enter the first number: "))
# second_num = int(input("Please enter the second number: "))
# third_num = int(input("Please enter the third number: "))

# number_list = [first_num, second_num, third_num]
# sorted_list = sorted(number_list, reverse=True)
# print(f"The largest number is: {sorted_list[0]}")

# Problem 4:
# Write a Python program that checks whether a given string is a palindrome or not. The program should ask the user for a string and then display an appropriate message.

# string = input("Please enter a string: ")

# for i in range(0, len(string)): 
#   if string[i].lower() != string[len(string) - 1 - i].lower():
#     print("The string is not a palindrome")
#     break

# if i + 1 == len(string):
#   print("The string is a palindrome.")

# Problem 5:
# Write a Python program that calculates the sum of all numbers from 1 to a given number. The program should ask the user for a number and then display the sum.

# num = int(input("Please enter a number larger than 1: "))
# sum = 0

# for i in range(0, num + 1):
#   sum += i

# print(f"The sum of all numbers from 1 to your given number, {num}, is {sum}")

# Problem 1:
# Write a Python function that takes a string as input and returns the number of vowels in the string. Test the function by asking the user for a string and displaying the number of vowels in it.

# def num_vowels(word):
#   vowels = "aeiou"
#   num_vowel = 0

#   for letter in word.lower():
#     for vowel in vowels:
#       if letter == vowel:
#         num_vowel += 1
  
#   return f"The number of vowels in the string is: {num_vowel}"

# string = input("Please enter a string: ")
# print(num_vowels(string))



### OPTIMIZED SOLUTION### 
# def num_vowels(word):
#     vowels = "aeiou"
#     num_vowel = sum(word.lower().count(vowel) for vowel in vowels)
#     return f"The number of vowels in the string is: {num_vowel}"




# Problem 2:
# Write a Python function that calculates the area of a circle. The function should take the radius of the circle as input and return the area. Test the function by asking the user for the radius of a circle and displaying the calculated area.

# import math

# def circle_area(radius): 
#   return radius * math.pi ** 2

# radius = int(input("Please enter a radius of a cirle: "))
# print(circle_area(radius))

# Problem 3:
# Write a Python function that checks whether a number is prime. The function should take an integer as input and return True if the number is prime and False otherwise. Test the function by asking the user for a number and displaying whether it is prime or not.

# import math

# def isPrime(num):
#   if num < 2:
#     return False

#   # Check for divisibility up to the square root of num
#   for i in range(2, int(math.sqrt(num)) + 1):
#     if num % i == 0:
#       return False
  
#   return True

# number = int(input("Please enter a number to check whether it's a prime: "))
# print(isPrime(number))

# Problem 5:
# Write a Python function that calculates the factorial of a given number. The function should take an integer as input and return the factorial. Test the function by asking the user for a number and displaying its factorial.

# def factorial(num):

#   fact = 1

#   for i in range(1, num + 1):
#     fact *= i
  
#   return fact

# number = int(input("Please enter a number: "))
# print(factorial(number))
