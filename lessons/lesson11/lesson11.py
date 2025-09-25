# Errors vs Exceptions
# Пайтон інтерпритована мова - і зазвачий помилки які ми отримуємо це run time errors

# в свою чергу вони діляться ще на 2: помилки синтаксичні і логічні(Exceptions)

# синтаксичні - помилки в назвах змінних, синтаксичних знаків мови програмування чи подібні речі
# ! вони виникають на моменті збору модуля перед виконанням і відразу якщо десь в можулі є синтаксична помилка - інтерпритатор видась її відразу до початку виконання коду в модулі.


# # print("Hello, World!"
# print("Hello, World!")
# def greet():
#     print("Hello, World!")
#     print("Welcome to Lesson 11."
#     print("Let's learn Python together!")

# greet()


# логічні - це типу "ділення нат 0" - або подібні - коли код не знає як йому опрацювати щось і впирається в помилку, або щось не можливо виконати - як ділення на 0
# ! ми не можемо логічні помилки наперед визначити однозначно (але якщо ми знаємо, що там може бути якась помилка - то ми її в коді заздалегісь опрацьовуємо)
#  ! робимо так звані ексепшени і попереджаємо помилку - і прописуємо що буде відбуватися у програми, якщо буде така-то помилка - програма виведе повідомлення що було не так і продовжить працювати, а не впаде через помилку.

# a = 10
# b = 10
# c = a / b
# print(c)


# для обробки помилок є ціла ієрархія в пайтон - і для кожної помилки ми можемо використовувити тип, який вже зазначений
# за посиланням внизу є дерево таких вбудованих вже ексепшенів: docs.python.org/3/library/exceptions.html
# головним буде клас BaseException - від нього є похідні і нам буде потрібен, як девам, його клас Exception і те що він містить в собі.
# якщо ми будемо створювати свої класи з ексепшенів, то наслідуємось саме від Exception, або від похідних від нього класів
# ! важливий момент як саме потрібно ловити помилки - їх не можна ловити в довільному порядку (якщо ми будемо переловлювати декілька помилок в одному ексепшені - маємо йти від унікальних до більш загальних) - бо він не перевіряє чи сталася саме помилка цього класу, а просто дивиться чи помилка є серед нащадків цього класу і може просто піти в Exception як таковий і тоді всі знизу будуть його нащадки і йому підійде - скаже що помилка з типом Exception, а це просто найзагальніший і ми не знаемо чи це якийсь імпорт еррор чи FileNotFoundError який наслідується від OSError, а той вже аж віж Exception

# BaseException - Базовий клас для всіх вбудованих винятків. Він не призначений для безпосереднього успадкування користувацькими класами.
# Exception - Усі вбудовані винятки, що не пов'язані з виходом із системи, походять від цього класу. Усі винятки, визначені користувачем, також повинні бути похідними від цього класу.
# ArithmeticError - Базовий клас для тих вбудованих винятків, що викликаються через різні арифметичні помилки.
# ZeroDivisionError - Виникає, коли виконується ділення або ділення по модулю на нуль для всіх числових типів.
# IOError - Виникає, коли операція вводу/виводу завершується невдачею, такою як оператор print або функція open) під час спроби відкрити файл, який не існує.
# IndexError - Виникає, коли індекс не знайдено в послідовності.
# KeyError - Виникає, коли вказаний ключ не знайдено в словнику.
# NameError - Виникає, коли ідентифікатор не знайдено в локальному або глобальному просторі імен.
# TypeError - Виникає, коли виконується спроба виконання операції або функції, яка є недійсною для вказаного типу даних.
# EOFError – Виникає, коли одна з вбудованих функцій (inputt) або необроблена _input()) досягає умови кінця файлу (EOF) без зчитування будь-яких даних.
# ValueError – Виникає, коли вбудована функція для типу даних має дійсний тип аргументів, але аргументи мають вказані недійсні значення.
# AttributeError – Виникає у разі невдалого посилання на атрибут або присвоєння.
# IdentationError – Виникає, коли ідентифікація неправильна.
# StopIteration – Виникає, коли метод next() ітератора не вказує на жодний об'єкт.
# SystemExit – Виникає функцією sys.exit().
# KeyboardInterrupt – Виникає, коли користувач перериває виконання програми, зазвичай натисканням CtrI+c.
# SyntaxError – Виникає, коли синтаксичний аналізатор зустрічає синтаксичну помилку.
# ImportError – Виникає, коли python не може знайти модуль.


# Проблема ексепшинів в тому, що вони припиняють роботу прошрами - але нам така поведінка не потрібна, то му ми відловлюємо помилку і опрацьовуємо її
# для цього в пайтон використовують блок try (Run this code)... except (Execute this code when there is an exception)
# але треба це робити в разі необхідності, а не усе обгортати в try - бо він сповільнює виконання програми
# трай бере на себе окремий процес програми - де має доступ до усього глобального. але спочатку пробує опрацювати код у себе - і якщо усе ок то синхронізує дані з основним потоком
# а якщо щось не так, то воно просто видалить цю частину окремо взятої пам'яті в якій спробувало виконати огорнутий в трай код і повернеться до початкової точки + виконає код який передбачений для помилки
# тому виконуємо try з усім, що зовнішнє - поля вводу, сервери, БД, отримання даних, файли
# якщо ми можемо вирішити через блок іфів - то краще так обійти - трай вже крайня межа.

# як використовуємо - приклад: (ділення на 0)
# try:
#     a = int(input("Enter a number: ")) # вводимо число
#     b = int(input("Enter another number: ")) # вводимо 0
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print ("Error: Division by zero is not allowed.")

# print("Program continues...")

# але в коді вище ми передбачили лише ZeroDivisionError - якщо введуть не числа - то програма вилетить через помилку введення ValueError
# якщо прописати except Exception - то буде переловлювати усе і не зупиниться програма, але ми не зможемо гнучко реагувати на помилки і підказати юзеру, що він ввів не те

# варіант щоб отримати об'єкт помилки і далі з ним працювати - запис у зміннe через as
# тоді можна отримати type(err).__name__ - і побачити яка саме помилка і показати її
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a / b
#     print(c)
# except Exception as err:
#     print("Error:", type(err).__name__, err)


# print("Program continues...")

# !!! важливо якщо на полі вводу натиснути ctrl+C - то буде помилка KeyboardInterrupt - але Exception її не піймає, бо вона від BaseException

# як переловлювати декілька помилок:
# в коді нижче може виникати 3 різні помилки:
# ValueError - якщо введемо в поле не число
# ZeroDivisionError - коли a буде = 3 в першій умові
# NameError - якщо не зайде програма в першу умову - не створиться змінна b - але зайде в другу умову, де неіснуюче b викликається

# щоб передати декілька - можна написати їх в тюпл except (ZeroDivisionError, NameError, ValueError) as err і опрацьовувати помилку, яка випаде
# але щоб окремо обробити кожну різним хендлером можна прописати декілька  except для кожної помилки
# якщо тнаписати except: (і не вказати помилку) - виконається на будь яку іншу яка вилетить - це є дефолтний ексепт
# і при такій обробці важливий стає порядок обробки помилок з дерева ексепшенів пайтон - бо якщо я наприклад як нижче стоїть ArithmeticError поставлю перед ZeroDivisionError - він ніколи не виконає ZeroDivisionError - бо відразу попаде на ширший клас який вже включає в себе ZeroDivisionError і виконає його.

# try:
#     a = int(input("Enter your number: ")) # throws ValueError if input is not an integer

#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#     # note that braces () are necessary here for multiple exceptions
# # except (ZeroDivisionError, NameError, ValueError) as err:
# #     print("Error Occurred and Handled", type(err).__name__, err)

# except ZeroDivisionError as err:
#     print("1", type(err).__name__, err)
# except ArithmeticError as err:
#     print("Error Occurred and Handled", type(err).__name__, err)
# except NameError as err:
#     print("2", type(err).__name__, err)
# except ValueError as err:
#     print("3", type(err).__name__, err)
# # except:
# #     print("Some other error occurred")




# else в обробці помилок: (No exceptions? Run this code)
# код з else виконується коли в блоці try не випало жодного ексепшену, а виконався саме код в try
# і також є блок finally - який виконується, щоб не виконалось вище - завжди! навіть якщо спрацював return вище - усе одно дійде до finally і виконає, а не завершить блок.
# для чого таке треба? - коли працюєм з чимось зовнішнім - наприклад, як зомбі процес - розказував приклад з закриттям файлу, коли програма завершилась, а був відкритий файл і ми не можемо файл закрити, бо процес висить - і треба грохати через диспетчер сам процес
# так як оперційна система виконує код, то по завершенню виконання коду операційці прилітає system exit, що сигналізує, щоб операційка закінцила процес виконання коду бо він завершився
# і вона закриває процес, але перед цим робить перевірку і може побачити що програма має відкритий файл і не завершити процес (але програму ми вже не бачимо, а процес висить)
# тому за допомогою finally ми можемо закрити процес, щоб операційка його виконала, навіть якщо відкритий файл
# тобто виконаються усі процеси і закриється 100%-во програма чи файл (але є ще контекстний менеджер і ми маємо про нього ще говорити і тоді не треба таке писати)

# try:
#     status_code = int(input("Enter status code: "))
# except ValueError as err:
#     print("Invalid input. Please enter a valid integer.", err)
# else:
#     if status_code == 200:
#         print("OK")
#     elif status_code == 404:
#         print("Not Found")
#     elif status_code == 500:
#         print("Internal Server Error")
#     else:
#         print("Unknown Status Code")
# finally:
#     print("Execution completed.")

# # print("Program continues...")
# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError as err:
#         print("Error: Division by zero is not allowed.")
#         return 0
#     except TypeError as err:
#         print("Error: Invalid input type. Please provide numbers.")
#         return -1
#     else:
#         return result
#     finally:
#         print("Execution of divide_numbers is complete.")
#         # return 99

# print(divide_numbers(10, 2))  # Should print 5.0
# print(divide_numbers(10, 0))  # Should handle division by zero
# print(divide_numbers(10, 'a'))  # Should handle invalid input type
# print("Program continues...")


# ми можемо примусово викликати помилку з raise
# часто в бібліотеках хентлери вже прописані і коли ми райзаємо якусь помилку - то хендлер відпрацьовує 
# томи ми можемо райзати усі помилки з набору в дереві ексепшенів і вони будуть відпрацьовувати (плюс додавати свої власні сповіщення на них в середині райз)
# The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception).
# 

# def read_file(file_path):
#     if not isinstance(file_path, str):
#         raise TypeError("File path must be a string.")
#     elif not file_path.endswith('.txt'):
#         raise ValueError("File must be a .txt file.")
#         # raise 10

# for i in ["document.txt", 123, "document.pdf"]:
#     try:
#         read_file(i)
#         print(f"{i}: File read successfully.")
#     except (TypeError, ValueError) as err:
#         print(f"{i}: Error - {type(err).__name__}: {err}")


# ми можемо створювати власні класи ексепшени
# їх часто навіть не особливо описують - більше заради назви і щоб було видно по назві точніше де помилка
# тобто по факту він дублює усе що є в Exception, але назву має таку. ЩО ВКАЗУЄ НА МОДУЛЬ або клас ДЕ ВИНИКАЄ ПОМИЛКА і ми чітко тоді можемо бачити куди йти виправляти
# додатково код у файлі models.py

# class CustomError(Exception):
#     """Custom exception class for demonstration."""

# def check_positive(number):
#     if number < 0:
#         raise CustomError("Negative value provided.")
#     else:
#         print("Positive value:", number)

# try:
#     check_positive(-5)
# except CustomError as err:
#     print("CustomError occurred:", err)


# try:
#     print("Start program")
#     result = function_sum(10, 20)
#     print("End program")
# except Exception:
#     print("We caught a bug")
# finally:
#     print ("Finish")


# def error_function():
#     raise ValueError()
#     print("Print from error_function")
#     return "String from error_function"

# def print_without_error():
#     print("Print from print_without_error")

# try:
#     print_without_error ()
# except ValueError:
#     print("We caught ValueError")
# else:
#     print("Print from else")
#     print(error_function())
# finally:
#     print("End of try...except")
# print("End of program")

my_list = [1,2,3,4,5]

try:
    print(my_list[5])
except Exception:
    print("We caught Exeption")
except IndexError:
    print ("We caught IndexError")