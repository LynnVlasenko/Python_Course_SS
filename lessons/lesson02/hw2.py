# Task 1

# 1.1 You need to write Python's philosophy in the string format
print("-------Task 1-------")

python_zen_text = " \
    Beautiful is better than ugly. \n \
    Explicit is better than implicit. \n \
    Simple is better than complex. \n \
    Complex is better than complicated. \n \
    Flat is better than nested. \n \
    Sparse is better than dense. \n \
    Readability counts. \n \
    Special cases aren't special enough to break the rules. \n \
    Although practicality beats purity. \n \
    rrors should never pass silently. \n \
    Unless explicitly silenced. \n \
    In the face of ambiguity, refuse the temptation to guess. \n \
    There should be one-- and preferably only one --obvious way to do it. \n \
    Although that way may not be obvious at first unless you're Dutch. \n \
    Now is better than never. \n \
    Although never is often better than *right* now. \n \
    If the implementation is hard to explain, it's a bad idea. \n \
    If the implementation is easy to explain, it may be a good idea. \n \
    Namespaces are one honking great idea -- let's do more of those! \n \
"

# find separately the number of occurrences of the words
# - "better", "never" and "is" in the given line
print('Task 1.1 _ find separately the number of occurrences of the words \n \
      - "better", "never" and "is" in the given line\n')


better_count = python_zen_text.count("better")
print(f"The number of occurrences of the words 'better' is {better_count}")

never_count = python_zen_text.count("never")
print(f"The number of occurrences of the words 'never' is {never_count}")

is_count = python_zen_text.count("is ")
print(f"The number of occurrences of the words 'is' is {is_count}")


# 1.2 you need to display all text in uppercase (all letters in uppercase)

print("\n------------------------------")
print('\nTask 1.2 _ to display all text in uppercase\n')

print(python_zen_text.upper())


# 1.3 replace all occurrences of the symbol “i” with “&”

print("\n------------------------------")
print('\nTask 1.3 _ replace all occurrences of the symbol “i” with “&”\n')

print(python_zen_text.replace("i", "&"))


# Task 2

# A four-digit natural number is specified:
print("-------Task 2-------")

number = input("Enter four-digit natural number: ")

print(f"Start number: {number}")

# 2.1 - find the product of the digits of this number

number_list = list(number)

product_result = 1
for i in number_list:
    product_result *= int(i)

print("\n------------------------------")
print (f"Task 2.1\n - The product of the digits of number is {product_result}")


# 2.2 - write the number in reverse order

print("\n------------------------------")

# first solution
print(f"Task 2.2\n - the number in reverse order: {number[::-1]}")

# second solution
reversed_number = "".join(list(reversed(number)))
print(f"- second solution: {reversed_number}")


# 2.3 - in ascending order, you need to sort the numbers included in the given number
print("\n------------------------------")
print(f"Task 2.3\n - in ascending order, you need to sort the numbers \n \
      included in the given number\n")

print("".join(sorted(number)))


# Task 3
# 3. Interchange the values of two variables without using the third variable.
print("\n-------Task 3-------")
print (f"Task 3\n - Interchange the values of two variables \n \
       without using the third variable.\n")

a = 1
b = 2
print(f"- initial values {a = } and {b = }\n")

a, b = b, a
print(f"- values after interchanging: {a = } and {b = }")