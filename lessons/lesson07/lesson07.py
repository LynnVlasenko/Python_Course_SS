# FUNCTIONS
# особливості:
# - функція створює власний скоуп (все, що описане в тілі функції - видиме лише в середині функції) (є з цим певні регулювання - команди global, local і nonlocal - далі описано)
# - функція в python завжди повертає щось - навіть якщо ми не пишемо return - повернеться None


# DOCSTRING
# описує роботу функції і коли ми її прописуємо для виклику, то IDE підсвічує нам цей опис
# !обов'язково має бути першим рядком в тілі функції - інакше буде помилка
# 
# def my_function():
#     """
#     This is a docstring for my_function.
#     """
#     print("Hello from my_function!")
# print(my_function)

# можна окремо підтягнути опис docstring, якщо він є:
# print(my_function.__doc__)
# або
# help(my_function)


# функція без виклику() - це об'єкт
# m = my_function
# print(m) # надрукує тип, назву і посилання на об'єкт функції

# функція в python завжди повертає щось - навіть якщо ми не пишемо return - повернеться None:
# print(f"{my_function()=}") - поверне None


# ПАРАМЕТРИ (передача аргументів функції)
# def print_name(name):
#     """
#     This is a docstring for print_name.
#     """
#     print(f"Hello, {name}!")

# print_name("Alice")
# print_name("Bob")

# RETURN
# return дозволяє нам вказати що має повернути функція
# !також важливо - після того, як функція виконала return - вона виходить з функції і припиняє виконання функції далі (тобто досягнули кінцевий результат і все - робота виконана)
# def absolute_value(num):
#     """
#     This function returns the absolute value of a number.
#     """
#     if type(num) in (int, float):
#         if num < 0:
#             return -num
#         return num
#     print("Error: Input must be an integer or float.")
# print(f"{absolute_value(-5)=}") 
# print(f"{absolute_value(3)=}")
# print(f"{absolute_value('3')=}")

# запис функції в один рядок - це lambda
# f = lambda x: x * x
# print(f(5))


# АРГУМЕНТИ і їх властивості в Python:
# Часто називають сигнатура функції або методу - це набір аргументів/параметрів, які ми можемо передавати у функцію

# Які можуть бути аргументи:
# Особливості:
# приймає рівно стільки аргументів, скільки є обов'язкових - якщо передамо у функцію більше або менше - помилка
# послідовність важлива! - як передамо аргументи так вони і розподіляються як вказано у функції (далі приклад) - тут гарно працюють Keyword arguments, щоб не переплутати чи правильно ми усе передаємо
# по типам! !! в python уважно, бо можна передавати будь-який тип у функцію - і регулювати приймати цей тип чи ні можна в тілі функції - прописуючи, якщо який тим - то що буде робити функція
# є чітка послідовність як можуть бути описані аргументи в середині функції: спочатку обов'язкові, потім *args, далі деформтні, і потім **kwargs

# Required arguments:
# def print_user_info(name, age, city):
#     """
#     This function prints the user's name and age.
#     """
#     print(f"Name: {name}, Age: {age}, City: {city}")

# типи даних, які можуть бути передані в аргумент.
# !! в python уважно, бо можна передавати будь-який тип у функцію - і регулювати приймати цей тип чи ні можна в тілі функції - прописуючи, якщо який тим - то що буде робити функція
# !! якщо прописати так як нижче - то IDE видасть рекомендацію щодо типу, який треба внести, але помилки не буде, якщо внесемо інший тип.
# Бо об'єкти в python працюють певним чином, що робить постійний пошук методів. бо методи не є в інстансах, насправді (будемо розбирати це на темі ООП)
# def print_user_info(name: str, age: int, city: str) -> None:
#     """
#     This function prints the user's name and age.
#     """
#     print(f"Name: {name}, Age: {age}, City: {city}")

# print_user_info("Alice", 30, "New York")
# print_user_info("Alice", 30) #TypeError: print_user_info() missing 1 required positional argument: 'city'
# print_user_info("Alice", 30, "Los Angeles", "temp") #TypeError: print_user_info() takes 3 positional arguments but 4 were given

# print_user_info(10, "30", 10)

# Default arguments:
# щоб параметр став не обов'язковим - йому треба призначити дефолтне значення.
# def print_user_info(name, age=18, city1="Unknown"):
#     """
#     This function prints the user's name and age.
#     """
#     print(f"Name: {name}, Age: {age}, City: {city1}")

# print_user_info("Alice")
# print_user_info("Alice", 30)
# print_user_info("Alice", 30, "Los Angeles")
# print_user_info("Alice", 30, "Los Angeles", 1) #TypeError: print_user_info() takes from 1 to 3 positional arguments but 4 were given
# print_user_info() #TypeError: print_user_info() missing 1 required positional argument: 'name'

# послідовність важлива! - як передамо аргументи так вони і розподіляються як вказано у функції (тут гарно працюють Keyword arguments, щоб не переплутати чи правильно ми усе передаємо)
# print_user_info("Los Angeles", "Alice", 30)

# Keyword arguments:
# можна прописувати при виклику назви параметрів і передавати їм значення, тоді не важливий порядок
# print_user_info(city1="Los Angeles", name="Alice", age=30)

# Variable-length arguments:
# параметри з зірочкою (*args) і двома зірочками (**kwargs), але назва може бути різна - головне вказати потрібну кількість зірочок
# * - каже, що параметр може приймати довільну кількість будь яких аргументів (в такому разі можна передати у функцію будь-яку кількість значень і помилок не буде) і це завжди буде тип tuple
# ** - каже, що параметр буде dict і коли ми передаємо в параметр з двома зірочками значеення з ключами, як у прикладі вище - то він їх запаковує в dict 
# def sum_numbers(*args, **kwargs):
#     """
#     This function returns the sum of two numbers.
#     """
#     print(f"{args=}")
#     print(f"{kwargs=}")
#     return sum(args) + sum(kwargs.values())
# print(sum_numbers(1, 2))
# print(sum_numbers(1, 2, 3, 4, 5))
# print(sum_numbers())
# print(sum_numbers(1,2,3,4, a=1, b=2)) # 1,2,3,4 попадає в args, a=1, b=2 в kwargs

# є чітка послідовність як можуть бути описані аргументи в середині функції: спочатку обов'язкові, потім *args, далі деформтні, і потім **kwargs
# def func(a, b, *args, d=1, c=2, **kwargs):
#     """
#     This function takes multiple arguments and keyword arguments.
#     """
#     print(f"{a=}, {b=}, {args=}, {d=}, {c=}, {kwargs=}")

# func(1, 2)
# func(1, 2, 3, 4, 5) # перші два значення присвоюються до обов'язкових, далі (3, 4 ,5) забере в *args, необов'язкові візьмуть свої дефолтні значення, kwargs пустий
# func(1, 2, 3, 4, 5, d=10, c=20, e=30) # перші два значення присвоюються до обов'язкових, далі (3, 4 ,5) забере в *args, у необов'язкові присвоїться d=10 і d=20, і в kwargs піде {e: 30}
# func(1, 2, 3, 4, 5, a=10, d=10, c=20, e=30) #TypeError: func() got multiple values for argument 'a' - до а намагаємось другий раз передати значення (бо перше обов'язкове має назву параметра a) - було б не А - то піде в kwargs
# func(1, a=2, 3, 4, 5, d=10, c=20, e=30)#SyntaxError: positional argument follows keyword argument

# інтерпретована функція print (як раз приймає *args - довільну кількість символів по факту і 2 необов'язкових параметра сепаратора і закінчення рядка)
# def my_print_str(*args, sep=" ", end="\n"):
#     result = sep.join(map(str, args)) + end
#     print(result)
#     return result
# s = my_print_str(1, 2, 3, 4, 5)
# s += my_print_str(1, 2, 3, 4, 5, sep=", ", end="!")
# s +=my_print_str(1, 2, 3, 4, 5, sep=", ", end="!")
# print(s)

# ! важливі нюанси щодо мютабле і інмютабле типів даних у функціях
# при такому записі в параметрах lst=[] - IDE буде сваритись, що в нас дефолтне значення мютабле обджект - його поведінка нижче прописана у виводах результатів
# тобто маємо використовувати для дефолтних значень тільки inmutable object або значення None
#  це тому, що сигнатура функції відноситьси не до тіла функції, а до неймінгу і виконуєтьсяи 1 раз
# сигнатура функції виконується в процесі оголошення функції, а не її виконання
# def function_add_one(lst=[]): 
#     lst.append(1)
#     print(lst)

# function_add_one() # [1]
# function_add_one([1, 2, 3]) # [1, 2, 3, 1]
# function_add_one() # [1, 1] - коли не передаємо значення - то мутує той об'єкт який заданий дефолтним - бо є референс на нього
# function_add_one([4, 5, 6]) # [4, 5, 6, 1]
# function_add_one()  # [1, 1, 1]

# використавши None за дефолтне значення зі створенням ліста в тілі функції - уникаємо такої проблеми
# def function_add_one(lst=None):
#     if lst is None:
#         lst = []
#     lst.append(1)
#     print(lst)


# function_add_one() # [1]
# function_add_one([1, 2, 3]) # [1, 2, 3, 1]
# function_add_one() # [1]
# function_add_one([4, 5, 6]) # [4, 5, 6, 1]
# function_add_one()  # [1]


# SCOPE - простір видимості функції та час життя змінних функцій

# Global scope - точка входу в неї створюється її глобальний скоуп - те що є видиме
# Модульний scope - кожен модуль(файл) має власний простір видимості - в межах файлу
# Local scope - тіло функції в середині файлу матиме свій окремий scope 
# Scope классів - теж мають власний скоуп в середині файлу

# def f():
#     a = 10
#     print(f"Inside f: {a=}")
# f()
# print(f"Outside f: {a=}") #NameError: name 'a' is not defined

# наразі модуть lesson07.py і являється глобальним скоупом - бо ми запускаємо саме його
# які нюанси взаємодії глобального скоупу зі скоупом функції?


# що буде коли викликати змінну з глобального скоупу в тілі функції? - буде працювати, але там писати не треба
# (бо це є відповідальність за те в чому ти невпевнений що існує) - бо якщо змінна перестане існувати в глобал - функція дасть помилку
# таке щось можуть використовувати при написанні фреймворку і є якийсь глобал конфіг файл - то можуть використовувати, але має бути дуже обгрунтовано
# правильно! - приймати значення як аргумент і з ним працювати 


# count = 0
# def info_count():
#     print(f"{count=}")
# info_count()
# count += 1
# info_count()
# del count
# info_count() #NameError: name 'count' is not defined. Did you mean: 'round'?

# # що буде коли модифікувати змінну з глобального скоупу в тілі функції? 
# у прикладі нижче буде помилка - бо python аналізує тіло функції, при її виклику. І дав помилку до самого першого виведення count, бо він проаналізував і зрозумів, що він насправді не знає що є таке count, бо його не створювали в тілі функції, а намагаються модифікувати
# count = 0
# def info_count():
#     # print(f"{count=}") #UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#     count += 1
#     print(f"{count=}")
# info_count()

# але якщо створити змінну з таким самим ім'ям в середині - python розумітиме, що це дві окремі змінні
# count = 0

# def info_count():
#     count = 0
#     count += 1
#     print(f"{count=}")

# info_count()
# print(f"g_{count=}")
# ---

# Але спочатку треба створити, а не викликати, якщо імена однакові з якоюсь змінною в глобал
# бо аналізуючи python бачить, що спочатку намагаюсь друкувати змінну з глобал, 
# а потім створюю таку саму змінну у функції і все - на цьому етапі, аналізуючи, він собі записав, що в нас є локальна така змінна і вже не дасть другувати її з глобал, 
# а дасть помилку, що така змінна має бути спочатку оголошена, а потім вже якісь дії з нею роби.

# count = 0
# def info_count():
#     print(f"{count=}") #UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#     count = 1
#     print(f"{count=}")

# info_count()
# print(f"g_{count=}")
# ---

# Але, якщо, я з якихось причин мені треба достукатись до глобальної і модифікуати - я можу за допомогою модифікатора global
# маю на самому початку тіла функції прописати global і перелічити через кому змінні, які я буду брати з global
# !!! Але - це можливо, коли це inmutable object
# count = 0
# def info_count():
#     global count
#     print(f"{count=}") #UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
#     count += 1
#     print(f"{count=}")


# info_count()
# print(f"g_{count=}")

# якщо беремо для модифікації з глобал mutable object - то йому усе одно і він змінюється без модифікатора
# !!! Але не варто так робити - беремо у функцію аргументи і там вже модифікуємо
# l = []
# def l2():
#     l.append(2)
#     print(f"{l=}")
# # def l2(l):
# #     l.append(2)
# #     print(f"{l=}")

# l2()
# l2()
# l2()
# print(f"{l=}")

# клас так не аналізується як функція 
# (клас це модуль в середині модуля по факту)


# ЗАМИКАННЯ
# Python знищкє об'єкт, коли на нього не має жодного посилання
# оголосили клас і перевизначили його конструктори del і init - автоматично викликаєтьсч при видаленні іс створенні, коли об'єкт зникає або з'являється
# class MyClass:
#     def __init__(self):
#         print(f"\tMyClass instance is created {id(self)=}")
        
#     def __del__(self):
#         print(f"\tMyClass instance is being deleted {id(self)=}")

# m = MyClass()


# def create_instance():
#     ins = MyClass()
#     return ins
# print("run function1")
# create_instance() # об'єкт створюється і видаляється
# print("end function1")
# print("run function2")
# i = create_instance() # об'єкт створюється і не видаляється, бо є присвоєння і буде посилання на нього
# print("end function2")
# print("end script") # усі створені об'єкти видаляються після завершення програми


# приклад замикання, виходячи з логіки зверху

def create_instance(num):
    my_num = num # записуємо передане у функцію значення в змінну
    def create(): # в середині функції створюємо іще одну - яка друкує створену змінну у попередній функції
        print(f"{my_num=}")
    return create # повертаємо референс на функцію

# по логіці зверху - змінна my_num мала ю припинити своє існування по відпрацюванню функції
# Але! - усе буде працювати при присвоєнні змінним функції і виклик змінної як функції


# a10 = create_instance(10)
# a20 = create_instance(20)

# a10()
# a20()
# a10()
# a20()
# у коді вище відбулось замикання - так як ми в середині функції create_instance замкнули функцію create 
# і потіп ще й присвоїли create_instance до змінних і викликали новостворенні змінні - так відбулось замикання і об'єкт не видалився з середини create_instance, бо ми його присвоїли у змінну a10 і a20

# create_instance(10)
# create_instance(20)
# # без присвоєння в змінну поверне <function __main__.create_instance.<locals>.create()>



# nonlocal - рух доступу до скоупу на 1 рівень вище(але не можна використовувати, коли на рівень вище це global - буде помилка)

# g = "global variable"
# def create_instance():
#     nonlocal g # SyntaxError: no binding for nonlocal 'g' found
#     g = "local variable"
#     def create():
#         nonlocal g
#         g = "inner variable"
#         print(f"create {g=}")
#     print(f"create_instance {g=}")
#     return create

# a = create_instance()
# a()
# print(f"{g=}")


# рекурсивна функція
# використовують часто в певних алгоритмах і структурах даних (для графів і дерев використовують)

# def factorial(n, level=0, line=""):
#     if n == 0:
#         # print(f"{'  ' * level}{line}1")
#         return 1
#     else:
#         # print(f"{'  ' * level}{line}factorial({n})")
#         line += f"{n}*"
#         return n * factorial(n-1, level+1, line)

# print(f"{factorial(5)=}")
# import sys
# sys.setrecursionlimit(6000)
# sys.set_int_max_str_digits(60000)
# print(f"{factorial(5000)=}")


# lambda функції - безименні однострічкові функції (особливість - час життя (так як безіменна відразу видаляється як відпрацювала, а звичана живе до моменту доки живе модуль))

# l = ["1", 10, 3.14,"test", -5, None, [1,2,3], (4,5,6), {7,8,9}, {"a":1, "b":2}]

# for item in l:
#     print(f"{item}: {type(item)}")
# # l.sort() #TypeError: '<' not supported between instances of 'int' and 'str'

# l.sort(key=str)
# print(l)

# def el(element):
#     if element is None:
#         return 0
#     elif isinstance(element, (int, float)):
#         return element
#     elif isinstance(element, str):
#         return len(element)
#     else:
#         return 100
# lam = lambda x: 0 if x is None else x if isinstance(x, (int, float)) else len(x) if isinstance(x, str) else 100
# l.sort(key=el)
# print(l)
# l.sort(key=lambda x: x if isinstance(x, (int, float)) else 0)
# print(l)


# def print_user_info(name, age, city):
#     """
#     This function prints the user's name and age.
#     """
#     return f"Name: {name}, Age: {age}, City: {city}"

# pui = lambda name, age, city: f"Name: {name}, Age: {age}, City: {city}"

# print(print_user_info("Alice", 30, "New York") == pui("Alice", 30, "New York"))


my_func = lambda x: x if x>5 else x**2*my_func (10)
print (my_func (2))


counter = 5
def my_func():
    counter = 8
    print (counter)
my_func()
print(counter)

def my_func(first_param = 3, second_param = 1):
    first_param = first_param + second_param
    second_param += 1
    print(first_param, second_param)
my_func (second_param = 1, first_param = 3)


def output_param (x, y, z):
    print(x, y, z)

my_tuple = (1, 2, 3)
output_param (*my_tuple)

# можуна передавати значення у функції в лісті, перебираючи їх
my_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for item in my_list:
    print(item(5))



# Task1. 
# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def get_largest_number(num1, num2):
  """
  Function with two positional arguments and returns the largest argument.
  """
  return max(num1, num2)

num1 = int(input("Enter a whole number"))
num2 = int(input("Enter another whole number"))

print(get_largest_number.__doc__)
print(get_largest_number(num1, num2))


# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

import math

def rectangle_area(length, width):
    """ Function to calculate the rectangle area """
    return length * width

def triangle_area(base, height):
    """ Function to calculate the triangle area """
    return 0.5 * base * height

def circle_area(radius):
    """ Function to calculate the circle area """
    return math.pi * radius * radius

geometric_figure = input("Enter the geometric figure name to get their area\n \
                         - ex: rectangle, triangle, circle): ")
# # зробити світч
# if geometric_figure.lower() == "rectangle":
#     length = float(input("Enter rectangle length: "))
#     width = float(input("Enter rectangle width: "))
#     print(f"Rectangle Area = {rectangle_area(length, width)}")
# elif geometric_figure.lower() == "triangle":
#     base = float(input("Enter triangle base: "))
#     height = float(input("Enter triangle height: "))
#     print(f"Triangle Area = {triangle_area(base, height)}")
# elif geometric_figure.lower() == "circle":
#     radius = float(input("Enter circle radius: "))
#     print(f"Area of Circle = {circle_area(radius)}")
# else:
#     print("I can calculates the area of a rectangle, triangle or circle only")

match geometric_figure.lower():
    case "rectangle":
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        print(f"Rectangle Area = {rectangle_area(length, width)}")
    case "triangle":
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))
        print(f"Triangle Area = {triangle_area(base, height)}")
    case "circle":
        radius = float(input("Enter circle radius: "))
        print(f"Area of Circle = {circle_area(radius)}")
    case _:
        print("I can calculates the area of a rectangle, triangle or circle only")


# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}


# solution with Counter
from collections import Counter

input_text = input("Enter some text to calculates the number of each character into it:")

def count_char(text):
    """Function to calculates the number of each character in a string"""
    text_l = text.lower()
    filtered_text = "".join(ch for ch in text_l if ch.isalpha())
    return dict(Counter(filtered_text))

print(f"Calculating result is {count_char(input_text)}")

# solution with loop
# def count_char(text):
#     """Function to calculates the number of each character in a string"""
#     result = {}
#     text_l = text.lower()
#     filtered_text = "".join(ch for ch in text_l if ch.isalpha())
#     for char in filtered_text:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     return result

# print(f"Calculating result is {count_char(input_text)}")

# solution with comprehension
# def count_char(text):
#     text_l = text.lower()
#     filtered_text = "".join(ch for ch in text_l if ch.isalpha())
#     return {char: filtered_text.count(char) for char in set(filtered_text)}

# print(f"Calculating result is {count_char(input_text)}")