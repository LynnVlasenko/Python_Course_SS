for num in range(2,-5,-1): # буде НЕ включно з -5
    print(num, end=", ")


numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers: # заходить в ітерацію - бере 0 індекс numbers за значення, що візьме в x / третя ітерація піднімається сюди, так як вкладений цикл повністю відпрацював і бере значення 1 індекса numbers для x
  for y in items: # заходить в ітерацію зі знаяенням 0 індекса numbers для x - і бере 0 індекс items за значення, що візьме в y / друга ітерація тут же, не повертаючись вище - залишається значення 0 індекса numbers для x і бере 1 індекс items для y / четверта і п'ята ітерація тут - зі значенням 1 індекса numbers для x і перебирає по черзі значення items для y
    print(x, y) # 1 друк: 10 Chair # 2 друк 10 Table # 20 Chair # 20 Table

var = 10
for i in range(10): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"i = {i}")
    for j in range(2, 10, 1): # [2, 3, 4, 5, 6, 7, 8, 9]
        print(f"\t j = {j}")
        print(f"\t {var % 2 == 0=}")
        if var % 2 == 0:
            continue
            var += 1 # ніколи не виконається код синтаксично прямо під continue - треби відступ назад на таб
            print(f"continue var += 1 = {var}") # ніколи не виконається - треби відступ назад на таб
        var += 1 # в такому разі код працюватиме, коли умова var % 2 == 0 не виконається і не спрацює continue
        print(f"continue var += 1 = {var}") # в такому разі код працюватиме, коли умова var % 2 == 0 не виконається і не спрацює continue
    var+=1
    print(f"i {var=}")
else:
    var+=1
    print(f"else {var=}")
print(var)


for num in range(10, 14): # [10, 11, 12, 13]
   print(f"num = {num}")
   for i in range(2, num): # [2, (3), 4, 5, 6, 7, 8, 9] / [(2), 3, 4, 5, 6, 7, 8, 9, 10] / [2, 3, 4, 5, 6, 7, 8, 9, 10, (11)] / [(2), 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
       if num%i == 1:
          print(f"i = {i}")
          print(num) # 10 # 11 # 12 # 13
          break


x = 0
while (x < 100):
   x+=2
print(x)


# Task1. Create a list that contains elements of integer type, then use
# the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

# with range
num_list = [1, 45, 6, 79, 10, 1, 5]

for i in range(len(num_list)):
    print(f"num_list[{i}]={num_list[i]}", end= " => ")
    num_list[i] = float(num_list[i]) # таким чином ми звертаємось до індекса і переписуємо туди значення
    print(f"num_list[{i}]={num_list[i]}")

print(num_list)

# with enumerate
# for elemnt  in enumerate([10, 20, 30, 40, 50]):
#     print(f"{elemnt=}")

num_l = [1, 45, 6, 79, 10, 1, 5]

for i, e in enumerate(num_l):
    print(f"num_l[{i}]={e}", end= " => ")
    num_l[i] = float(e) # таким чином ми звертаємось до індекса і переписуємо туди значення
    print(f"num_l[{i}]={num_l[i]}")

print(num_l)



# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)


n = int(input("Enter some Fibonacci number: "))
i = 0
# f_num_first = 0
# f_num_second = 1
fib_list = [0, 1]
if n == 0:
    print(n)
else:
    while n != i:
        print(n != i)
        if n == 0:
            break
        print(fib_list)
        i = fib_list[-1]
        print(f"{i=}")
        print(f"{n=}")
        fib_list.append(fib_list[-1]+fib_list[-2])

    

# Task3. Write a script that will calculate the factorial of the entered
# number without using recursion.
# Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6, ….

number = int(input("Enter some integer: "))

number_list = list(range(1, number+1))

factorial = 1
for i in number_list:
    factorial *= int(i)
    print(f"{i=}")
    print(f"{factorial=}")


print(f"Factorial of the entered number = {factorial}")






word = input()

unique_letters = set()
is_isogram = True

for letter in word.lower():
    if letter in unique_letters:
        is_isogram = False
        break
    unique_letters.add(letter)

print(is_isogram)

# You are given a variable decimal that contains an integer value read from input(). Write a program that prints the binary (base-2) representation of this decimal (base-10) number as a string, without leading zeros. If the given decimal value is 0, your program must print 0. 

# To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

# Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).

# For example:

# If decimal = 0, print: 0
# If decimal = 5, print: 101
# If decimal = 255, print: 11111111
# Important:
# Your program should print only the final binary string representation. Make sure to print exactly what is required.

# Note:
# The input decimal value will always be less than 1024.

# Input	Expected
# 0	0
# 5	101
# 255	11111111
# 9	1001
# Відповідь:(penalty regime: 0 %)


decimal = int(input())

# via loop
# If input is 0 - print "0".
if decimal == 0:
    print(0)
else:
    # Otherwise, keep dividing the number by 2
    binary = ""
    while decimal > 0:
        # The remainder (% 2) is the next binary digit.
        remainder = decimal % 2
        # Prepend each remainder to the binary string.
        binary = str(remainder) + binary
        # Get a decimal number after integer division
        decimal //= 2
    # When the decimal reaches 0, we have the full binary representation.
    print(binary)

# via method bin
# print(bin(decimal)[2:])  # 101   (без префікса "0b")



# You are given an integer n, which is already provided in the variable n by reading input(). Your goal is to create a function that calculates the mean of all digits in this number. The mean is determined by summing all the individual digits of n and then dividing this sum by the total number of digits.

# For example,

# if n is 512, the sum of its digits is 5 + 1 + 2 = 8, there are 3 digits in total, and so the mean is 8 / 3 = 3.
# The tests expect the mean to be an integer (already rounded). After calculating the mean, store it in a variable named result.

# Make sure not to print anything to the console, since the testing system will check your solution by looking directly at the value stored in result.

# For example

# Tests	Input	Expected
# print(result)	42	3
# print(result)	12345	3
# print(result)	1024	2


n = int(input())

# n_str = str(n)
# n_sum = 0

# for i in n_str:
#     n_sum += int(i)

# result = round(n_sum/len(n_list))
# print(result)

# другий спосіб
digits = [int(d) for d in str(n)]

average = sum(digits) // len(digits)
print(average)



# You are given a string stored in the variable word, which is already read from input(). Your task is to write a program that prints the number of vowels contained in this string. Only the letters a, e, i, o, and u are considered vowels (not y). All test cases will consist of a single word containing only lowercase letters.

# Make sure your program prints the total count of vowels to the console.

# Input 	Expected
# apple	2
# queue	4
# sky	0
# hello	2
# Option	2
# Відповідь:(penalty regime: 0 %)

word = input()

vowels_number = 0 
for i in word:
    if i in ["a", "e", "i", "o", "u"]:
        vowels_number += 1
print(vowels_number)


word = input()
print(sum(i in "aeiou" for i in word))


# You are given a number as a string stored in the variable binary_number, which has already been read from input(). Write code that creates a list of boolean values by iterating through this number: convert each 1 into True and each 0 into False. Finally, print this list.

# The input will contain  only the digits 0 and 1.

# For exaple

# Input	Expected
# 101	[True, False, True]
# 0000	[False, False, False, False]
# 1111	[True, True, True, True]
# 10	[True, False]


binary_number = input()

boolean_list = []
for i in binary_number:
    if int(i):
        boolean_list.append(True)
    else:
        boolean_list.append(False)
print(boolean_list)

# or

boolean_list2 = [True if int(i) else False for i in binary_number]
print(boolean_list2)




# You are given a variable list_int that reads a string of comma-separated integers from input(). 
# Write a program that converts this input into a list of integers and prints this original list. 
# Then, using a loop, change each element from an integer (int) to a floating-point number (float), 
# and print the updated list list_float where all elements are of type float. 
# Be sure to print both the initial and the modified list.

# Hint: use the built-in float() function for the conversion.

list_int = input()

list_int = list_int.replace(",", " ").split()
list_float = []

# -------- with range ---------
# for i in range(len(list_int)):
#     list_int[i] = int(list_int[i])
# print(list_int)

# for i in range(len(list_int)):
#     list_float.append(float(list_int[i]))
# print(list_float)

# -------- with enumerate ---------
# for i, e in enumerate(list_int):
#     list_int[i] = int(e)
# print(list_int)

# for i, e in enumerate(list_int):
#     list_float.append(float(e))
# print(list_float)

# -------- with list comprehension ---------
list_int = [int(e) for i, e in enumerate(list_int)]
print(list_int)

list_float = [float(e) for i, e in enumerate(list_int)]
print(list_float)
