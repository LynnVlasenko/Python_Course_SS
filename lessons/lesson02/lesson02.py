# b = True
# print(type(b), b)

# # a = 999**9999
# # import sys
# # sys.set_int_max_str_digits(99999)
# # print(len(str(a)))

# print(set("sdfgsdhgfjsdhgfhdsgfjhdsgfhsdgfjhdsgjhfgdsjhgfsdhfdsgfdjsfgjdhgsdj"))


# s = "test"
# print(id(s), s)
# print(s[0])
# # s[0] = "5"
# s += "rrr"
# print(id(s), s)

# l = [1,2,3]
# print(id(l), l)
# l.append("4")
# print(id(l), l)

# print(type(s), str, type(s) is str)
# print(type(l), list)

# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# l3 = l1

# print(f"{l1} {id(l1) =}")
# print(f"{l3} {id(l3) =}")
# print(f"{l2} {id(l2) =}")
# print(f"{l1 is l3=}")
# print(f"{l1 is l2=}")
# print(f"{id(l1) == id(l2) =}")
# print(f"{l1 == l2=}")
# a = 1+2+3 \
#     +4+5+6 \
#     +7+8+9
# print(a)
# a = (1+2+3 
#     +4+5+6 
#     +7+8+9)
# print(a)
# a = (1+2+3 
#     +4+5+6 
#     +7+8+9, )
# print(a)
# a = [1+2+3 
#     +4+5+6 
#     +7+8+9]
# print(a)

# a = 1; b=2; c=3
# print(a, b, c)
# a = 1
# b = 2
# c = 3
# print(a, b, c)
# a, b, c = 1, 2, 3
# print(a, b, c)

# for i in range(2):
#    print(i)
#    for j in range(2):
#     print("\t=>", end="\t")
#     print(f"{i}-{j}", end="\t")
#     print("||")
#    print(f"end {i}")

# a = b = c = d =5
# a = 5
# b = a
# c = a
# d = a

# for i in range(270):
#     t = str(i)
#     t = int(t)
#     print(f"{i} {i is t}")


# a = 10
# print(a)
# a = 0b10 # 0 1
# print(a)
# a = 0o17 # 0 1 2 3 4 5 6 7 
# print(a)
# a = 0x1f # 0 1 2 3 4 5 6 7 8 9 a b c d e f
# print(a)
# a = 100_000_00_0_00_000_000
# print(a)
# a = 15.5
# print(a)
# a = .5
# print(a)
# a = 1.
# print(a)
# a = 1e5 # 1 * 10 ** 5
# print(a)
# a = 1e-3 # 1 * 10 ** -3
# print(a)

# print((-1)**(0.5))
# print(True == 1)
# print(True == 2)
# print(False == 0)
# print(15 + True + False + 1)


# a = [1,2,3]
# print(type(a), a)

# a = (1,2,3)
# print(type(a), a)

# a = {1, 2, 3}
# print(type(a), a)

# a = {
#     1 :1,
#     "2":"test",
#     3:"test3"
# }
# print(type(a), a)
# a = {}
# print(type(a), a)
# a = set("fashdgfsahgdfsahgfdsah")
# print(type(a), a)

# print(int("123"))
# # print(int("123a"))
# print(int("123a", 30))
# # print(int("123a", 99))

# s = {1,2,3}
# st = str(s)
# print(st[0])
# print(st[1])
# print(str(s))

# t = "text"
# print(list(t))
# print(tuple(t))
# # print(tuple(1))#TypeError: 'int' object is not iterable
# x = 20
# print(bin(x))
# print(oct(x))
# print(hex(x))

# text = "VJKv6T*807t0"
# for c in text:
#     print(f"{c} - {ord(c)}") # виведе номер id симиола у таблиці ASCII
# for i in range(255):
#     print(f"{i} - {chr(i)}") # виведе символ, що відповідає номеру id в таблиці ASCII

s = "dsvbfdbfd" \
"" \
"" \
"sdv" \
"sdv" \
""
print(s)

s = "dsvbfdbfd\n" \
"trghjy78\n" \
"\n" \
"sdv\n" \
"sdv\n" \
"\n"
print(s)

s = """
sdvds
v
sdv
ds

dsv
sd

"""
print(s)

unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"  # r вимикає екранування # - результат сира стрічка (raw \n string)

print(unicode) # Ünicöde
print(raw_str) # raw \n string

# t = "abc\ncde"
# print(t)

# t = "0123456789\rabc"
# print(t)
# t = "012\t3456789"
# print(t)
# t = "012\t34\"56789"
# print(t)
# t = "012\t34\\56789"
# print(t)
# # abc3456789


# template = "%s is %d years old. Your sallary is %.3f $"
# print(template)
# print(template % ("Liubomyr", 39, 100))
# print(template % ("Ira", 18, 10000.9987))
# # print(template % ("Ira", "18", 10000.9987))TypeError: %d format: a real number is required, not str
# print(round(10000.9987, 3))
# template = "{} is {} years old. Your sallary is {:.3f} $"
# print(template.format("Liubomyr", 39, 100))
# print(template.format("Liubomyr", "39", 100))
# template = "{name} is {age} years old. Your sallary is {s:.3f} $ {name}"
# print(template.format(age="39", s=100, name="Liubomyr"))

# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print(default_order)
# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print(positional_order)
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print(keyword_order)

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
#'Binary representation of 12 is 1100'
# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
#'Exponent representation: 1.566345e+03'
# round off
print("One third is: {0:.3f}".format(1/3))
#'One third is: 0.333'

# z = 2
# text = input("text: ")
# print(f"text {z**4 =} {text[:20]:<20}|")

name = "Liubov"
age = "20"
message = ( f"Hi {name}. " f"You are {age} years old. " )
print(message)

name = "Liubov"
age = "20"
message = ( f"Hi {name}. " "You are {age} years old. " )
print(message)

import datetime
name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)
f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'
'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
f'He said his name is {name!r}.'
"He said his name is 'Fred'."

# f ' <text> { <expression> <optional !s, !r, or !a> <optional : format specifier> } <text> ... '

text = "SoftServe"
# print(text[0])
# print(text[1])
# print(text[2])
# # print(text[20])#IndexError: string index out of range
# print(text[-1])
# print(text[-2])
# # print(text[-20])#IndexError: string index out of range
# print(text[1:5]) # індекс з 1 по 5 (не вклюно!)
# print(text[:5])
# print(text[2:])
# print(text[:])
# print(text[::2]) # третій параметр - це крок - кожну другу літеру візьме з вказаного діапазону
# print(text[::3])
# print(text[1:-3:2])
# print(text[5:-6]) # не існуючий діапазон який наліз один на одного не дає помилки, але вивеле пусту стрінгу

# print("A",text.center(50), "A")
# print("A",text.center(50, "*"), "A")
# print("A","  vdsc   ds vds fv ds   ".strip(), "A")
# print("A","  vdsc   ds vds fv ds   ".lstrip(), "A")
# print("A","  vdsc   ds vds fv ds   ".rstrip(), "A")
# print("j hiub non o non io ni b ijb i".split())
# print("j hiub non o non io ni b ijb i".split("non"))
# print("".join(["1","2","3","4","5"]))
# print(" => ".join(["1","2","3","4","5"]))
l = [1,2,"tets",4]
print(l)
for i in str(l):
    print(f"{i}", end="_")

for i in l:
    print(f"{i}", end="_")

s1 = "hot"
s2 = "dog"
print(s1 + s2)

first_name = "television"
hobby = "homer"
tmp = first_name
first_name = hobby
hobby = tmp
print(f"T{first_name[1:3]} likes to watch {hobby[4:]}")

str = "my name is James bond"
print (str.capitalize())

print("John" > "Jhon")
print("Emma" < "Emm")

str1 = 'Welcome'
print(str1*2)

str1 = "My salary is 7000"
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())

str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub, 4))


minutes = int(input("Enter minutes to convert to seconds: "))
convert = minutes*60
print(f"In {minutes} minute(s) {convert} seconds")


R = int(input())
r = int(input())

PI = 3.14

result = round((4/3) * PI * (R ** 3 - r ** 3), 2)
print(result)


base = int(input())
height = int(input())

tri_area = 1/2 * base * height
print(tri_area)


number = int(input())
number += 1
print(number)

#incremented_number = number + 1
#print(incremented_number)


num1 = int(input())
num2 = int(input())

result = num1 % num2
print(result)


