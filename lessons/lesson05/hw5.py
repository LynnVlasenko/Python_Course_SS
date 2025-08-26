# You are given a string that has already been read from input() and stored in the variable lst. 
# This string contains a list of distinct integers separated by commas. 
# You are also given an integer n (already read from input()), which represents the position of the smallest integer to find 
# (the smallest integer is the first smallest, the second smallest integer is the second smallest, and so on).

# Your task is to convert the string into a list of integers, then find the nth smallest integer in the list 
# (where n is 1-based, i.e. 1 gives the smallest, 2 gives the second smallest, etc.). 
# If n is larger than the size of the list (out of bounds), set result to None. 
# Otherwise, store the found integer in result.

# Do not print anything to the console, 
# as the testing system will check the value stored in result.

# lst = input()
# list_int = list(map(int, lst.replace(",", " ").split()))
# n = int(input())

# result = [None if n > len(list_int) else sorted(list_int)[n-1]]
# # потрібен просто int
# result = None if n > len(list_int) else sorted(list_int)[n-1]

# спосіб через простий if
# if n > len(list_int):
#     result = None
# else:
#     result = sorted(list_int)[n-1]
        

# You are given a string stored in the variable lst, which has already been read from input(). 
# This string contains a list of numbers separated by commas. 
# Your task is to convert this string into a list of integers, 
# and then create a new list where each element is increased by its index in the list 
# (that is, add 0 to the first element, 1 to the second element, 2 to the third, and so on). 
# Store the final list in the variable result.

# Do not print anything to the console, as the testing system will check the value stored in result.


# lst = input()
# list_int = list(map(int, lst.replace(",", " ").split()))
# result = [v+i for i, v in enumerate(list_int)]
# print(result)



# You are given a string that has already been read from input() and stored in the variable lst. 
# This string contains a list of integers separated by commas. 
# Your task is to convert this string into a list of integers, 
# then create a new list that contains only the integers that appear an odd number of times in the original list. 
# Each such integer should appear only once in the result, even if it appeared multiple times in the original list. 
# Store this new list in the variable result. 


lst = input()

list_int = list(map(int, lst.replace(",", " ").split()))

# result = []
# for n in list_int:
#     print(n)
#     if list_int.count(n) % 2 == 1 and n not in result:
#         result.append(n)

result = [n for n in set(list_int) if list_int.count(n) % 2 == 1]

print(result)


# You are given a string that has already been read from input() and stored in the variable lst. 
# This string contains elements separated by commas, and these elements can be anything: integers (positive or negative), 
# floating point numbers, or words. Your task is to create a new list that contains only the positive integers, 
# removing all not valid values. Store the resulting list of integers in the variable result.

# Do not print anything to the console, as the testing system will check the value stored in result.

lst = input()

result = [int(i) for i in lst.replace(",", " ").split() if i.isdigit()]

# or
# lst = lst.replace(",", " ").split()
    
# result = []

# for i in lst:
#     if i.isdigit():
#         result.append(int(i))

print(result)


# You are given a string that has already been read from input() and stored in the variable lst. 
# This string contains a list of numbers separated by commas. 
# You are also given an integer num, which has already been read from input(). 
# Your task is to convert the string into a list of integers 
# and then calculate the probability (in percent) of selecting a number from the list that is greater than or equal to num. 
# The probability should be expressed as a percentage, rounded to one decimal place, and stored in the variable result. 

# Use the formula:
# Percent probability of event = 100 * (number of favorable outcomes) / (total number of possible outcomes)

lst = input().strip()
num = int(input().strip())

list_int = list(map(int, lst.split(",")))

# number of favorable outcomes
favorable = sum(1 for n in list_int if n >= num)

# total number of possible outcomes
total = len(list_int)

result = round(100 * favorable / total, 1)
print(result)

# !!!! викликала del sum - бо не працював код favorable = sum(1 for n in list_int if n >= num)
# del sum  # - повертає вбудовану функцію sum 
# (в мене була помилка 'int' object is not callable)
# - це говорило про те, що десь було створено змінну з іменем sum і вона перезаписалась, 
# щоб повернути при таких помилках треба робити команду del sum, або інша функція, якщо видає на ній подібну помилку)