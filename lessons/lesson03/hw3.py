# Write a script, which of the two entered
# numbers will determine which of them is
# more and which is less. Take into account
# the case of equality of numbers.

num1 = int(input())
num2 = int(input())

if num1 > num2:
    print("num1 > num2")
elif num1 < num2:
    print("num1 < num2")
else:
    print("num1 = num2")



# Write a script that will check whether
# the entered number is even or odd and
# display the appropriate message.

num1 = int(input())

print("even") if num1 % 2 == 0 else print("odd")


# Task1. "Temperature Converter"
# Write a Python program that prompts the user to enter a temperature in Celsius and then
# converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. Your program should then
# print out the converted temperature in Fahrenheit.
# However, if the user enters a temperature below -273.15°C (the lowest possible
# temperature in the universe, also known as absolute zero), your program should print an
# error message instead of attempting to convert the temperature.

# Note: You can assume that the user will enter a valid input (a number for the temperature in Celsius).

# Example output:
# Enter the temperature in Celsius: 25
# 25°C is equivalent to 77°F

# Example output (if the user enters a temperature below absolute zero):
# Enter the temperature in Celsius: -300
# Error: Temperature below absolute zero (-273.15°C)

celsius_temp = float(input("Enter the temperature in Celsius: "))
fahrenheit_temp = ((celsius_temp * 9/5) + 32)

print("Temperature below absolute zero (-273.15°C)") if celsius_temp < -273.15 else print(f"{celsius_temp:.0f}°C is equivalent to {fahrenheit_temp:.0f}°F")


# You are given a variable number, which has already been read from input as a string.

# Write a Python program that first checks whether the provided input is a valid whole number. 
# This means it can either be a non-negative integer (for example "123") or a negative integer (for example "-45"). 
# If the input is not a valid whole number, assign the string "Wrong data type" to the variable result.

# If it is a valid number, convert it to an integer and determine the total count of its digits, ignoring any negative sign. 
# For example, for 123, count_digits is 3; for -23, it is 2; and for 3, it is 1. Finally, store this count in the variable result.

#  Do not print anything; the testing system will check the value stored in result.
# https://www.geeksforgeeks.org/python/check-if-a-number-is-a-whole-number-in-python/


number = input()
# print(number)
result = 0 

try:
    number_int = int(number)
    print("Whole number")
    
    number_str = str(number_int)
    if number_str[0] == "-":
        result = len(number_str[1:])
    else:
        result = len(number_str)
    print(result)
    # if number_int % 1 == 0:
    #     print("Whole number")
    # else:
    #     result = "Wrong data type"
except ValueError:
    result = "Wrong data type"
    print(result)


# You are given an integer variable grade that has already been read from input 
# and represents a numeric grade between 0 and 100. 
# Write a Python program that uses conditional statements to determine 
# and assign the corresponding letter grade based on the following scale:

# A for grades from 90 to 100
# B for 80 to less than 90
# C for 70 to less than 80
# D for 60 to less than 70
# E for 50 to less than 60
# F for grades from 0 to less than 50.
# If the provided number is less than 0, assign the message "Wrong number" instead.
# Store the resulting letter grade or message in the variable result.

# Do not print anything; the testing system will check the value of result.

# Відповідь:(penalty regime: 0 %)

grade = int(input())

# if grade < 0:
#     result = "Wrong number"
#     print(result)
# elif 90 <= grade <= 100:
#     result = 'A'
#     print(result)
# elif 80 <= grade < 90:
#     result = 'B'
#     print(result)
# elif 70 <= grade < 80:
#     result = 'C'
#     print(result)
# elif 60 <= grade < 70:
#     result = 'D'
#     print(result)
# elif 50 <= grade < 60:
#     result = 'E'
#     print(result)
# elif grade < 50:
#     result = 'F'
#     print(result)
# else:
#     result = "Wrong number"
#     print(result)


match grade:
    case g if g < 0:
        result = "Wrong number"
        print(result)
    case g if 90 <= g <= 100:
        result = 'A'
        print(result)
    case g if 80 <= g < 90:
        result = 'B'
        print(result)
    case g if 70 <= g < 80:
        result = 'C'
        print(result)
    case g if 60 <= g < 70:
        result = 'D'
        print(result)
    case g if 50 <= g < 60:
        result = 'E'
        print(result)
    case g if g < 50:
        result = 'F'
        print(result)
    case _:
        result = "Wrong number"
        print(result)



# You are given three integer variables num1, num2, and num3, which have already been read from input(). 
# Write a Python program that sorts these three numbers in ascending order and prints them on a single line separated by spaces. 
# You must implement the sorting logic using only if and else statements; 
# do not use any built-in sorting functions or data structures like lists.

# Make sure your program prints the three numbers in increasing order regardless of their initial input order.

num1 = int(input())
num2 = int(input())
num3 = int(input())


if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle, largest = num2, num3
    else:
        middle, largest = num3, num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle, largest = num1, num3
    else:
        middle, largest = num3, num1
else:
    smallest = num3
    if num1 <= num2:
        middle, largest = num1, num2
    else:
        middle, largest = num2, num1
print(smallest, middle, largest)



# You are given three variables that have already been read from input(): 
# number1 and number2 as integers, and operator as a string 
# that represents one of the four basic arithmetic operations (+, -, *, /). 
# Write a Python program that uses only an if, elif, else structure 
# to perform the corresponding calculation based on the operator and print the result. 
# If the provided operator is not one of the four supported, print the message "Wrong operator" instead.

number1 = int(input())
number2 = int(input())
operator = input() # (+, -, *, /)

# if operator == "+" or operator == "-" or operator == "*" or operator == "/":
#     result = f"{number1} {operator} {number2}"
#     print(f"{result =}")
# else:
#     print("Wrong operator")

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 == 0:
        print("Division by zero is not allowed.")
    result = number1 / number2
else:
    result = "Wrong operator"

print(result)

# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#     print('False')


# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#         print (f"x = x + 5 = {x}")
#     elif a > 5:
#         x = x + 4
#         print (f"x = x + 4 = {x}")
#     else:
#         x = x + 3
#         print (f"x = x + 3 = {x}")
# else:
#     x = x + 2
#     print (f"x = x + 2 = {x}")
# print(x)


# x = 100
# y = 50
# print(x and y)


# if False:
#     print("Nissan")
# elif True:
#     print("Ford")
# elif True:
#     print("BMW")
# else:
#     print("Audi")


# if "cat" == "dog":
#     print("prrrr")
# else:
#     print("ruff")


# if 2 == 2:
#     print("ice cream is tasty!")


# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# if -3:
#     print("true")


# if 5 > 10:
#     print("fan")
# elif 8 != 9:
#     print("glass")
# else:
#     print("cream")


# x = 5
# if x > 0:
#     x += 1
# if x < 10:
#     x += 1
# else:
#     x -= 1
# print(x)


# num1 = 10
# num2 = 20
# result = num1 if num1 < num2 else num2
# print(result)


# x = 5
# if x < 10:
#     x += 1
#     if x < 5:
#         x += 2
# x -= 1
# print (x)

# x = 10
# if x > 5:
#     print("Greater than 5")
# if x < 15:
#     print("Less than 15")


# num = 7
# result = "Even" if num % 2 == 0 else "Odd"
# print(result)

# x = 10
# y = 5
# if x > y:
#     result = x + y
# else:
#     result = x - y
# print(result)


# x = 10
# if x > 5:
#     if x > 8:
#         print("A")
#     else:
#         print ("B")
# else:
#     print("C")


# x = 42
# if x > 40 and x < 50: 
#     if x % 2 == 0:
#         print("A")
#     elif x % 3 == 0:
#         print("B")
# else:
#     print("C")


# x = 20
# y = 10
# if x >= y and x != 10 and (y % 2 == 0 or x % 4 == 0):
#     print("A")
# else:
#     print("B")


# x = 10

# match x:
#     case int(value):
#         if value < 0:
#             print("Negative integer")
#         else:
#             print("Non-negative integer")
#     case str(value):
#         print("String")
#     case _:
#         print("Other")

# number = int(input())

# print(number)

# print("True") if number % 5 == 0 else print("False")


# word = input()

# # if len(word) >= 2:
# #     print(f"{word[0:2]}...{word[0:2]}...{word}?")
# # else:
# #     print("oh...")

# print(f"{word[0:2]}...{word[0:2]}...{word}?") if len(word) >= 2 else print("oh...")


# word = input()

# x_count = word.lower().count("x")
# o_count = word.lower().count("o")

# if x_count == 0 and o_count == 0 or x_count == o_count:
#     print("True")
# else:
#     print("False")


# card = input()

# # text = input("text: ")
# # print(f"{text:>16}|")

# if card.isdigit() and len(card) >= 16:
#     print(f"{"*"*12}{card[12:17]}")
# else:
#     print("Invalid card")

# # print("*"*12)


# card = input()

# if card.isdigit() and len(card) >= 16:
#     # print(f"{"*"*12}{card[12:17]}") - в VSCode працювало - тут дає помилку "SyntaxError: f-string: expecting '}'"
#     print(f"************{card[12:17]}")
# else:
#     print("Invalid card")


# st = input()

# if st.isdigit(): 
#     print(st)
# else:
#     print("Not a number")


# number = int(input())

# print(number) if number == 0 or number < 0 else print(-number)


# num1 = int(input())
# num2 = int(input())

# print("True") if num1 == 10 or num2 == 10 or (num1 + num2) == 10 else print("False")


