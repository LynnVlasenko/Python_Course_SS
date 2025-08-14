# a = 1
# b = 2
# print(a>b) # false
# print(a<b) # true

# можна порівнювати не лише числа, а і будь що ітерабельне (list, tuple, string..)
# !але не можна порівнювати різні типи

# порівняння стрінги, віджбувається за їх порядковим номером в таблиці символів, 
# або якщо значення рівні, але потім рядок просто довший, то він вважається більшим 
# (як у прикладі "21" і "2")
# a = "21"
# b = "2"
# print(a>b) # True
# print(a<b) # False

# a = ["21"]
# b = ["2"]
# print(a>b) # True
# print(a<b) # False

# a = ["21"]
# b = 1 
# помилка тут - різні типи (+ число не ітерабельне)! 
# (перевірка завжди іде спочатку з лівої частини порівняння (чи є така дія в лівому). 
# і потім чи є така дія в правому - якщо нема ні там не ні там - отримаємо ексепшн помилку)
# # print(a>b) #TypeError: '>' not supported between instances of 'list' and 'int'
# # print(a<b) #TypeError: '>' not supported between instances of 'list' and 'int'

# порівняння з логічними операторами and, or. not
# !пріорітет - спочатку and спрацює - потім or

# a = int(input("a:"))

# print(a >=18 and a <=65)
# аналогічний і корочший запис того, що вище
# print(18 <= a <= 65) 

# print(a < b and b < c and c < d)
# аналогічний і корочший запис того, що вище (можна не писати and - за замовчуванням буде рахуватись як and)
# print(a< b < c <d) 

# Що повертають and або or?
# в більшості мов програмування - булеві значення
# але в Python - ні: (повертає не булеві значення, а повертає об'єкти)

#AND
# and повертає останній істиний об'єкт, якщо всі елементи були істинні, або перший не істиний
# print(89 and [1,2,3]) # поверне [1,2,3]
# print(89 and [1,2,3] and 0 and "sfds") # так як 0 - не істиний - повернувся він.

#OR
# or повертає перший істиний або останній неістиний, якщо усі були неістині
# print(0 or None or 10 or "test" or "") # поверне 10
# print(0 or None  or "" or []) # поверне пустий ліст = [] - бо це неістинне

# що вважає не істиною?
# is_false = [False, None, 0, 0.0, "", [], (), {}] 
# "", [], (), {} - все, що ітерабельне, якщо воно не містить елементів (його довжина є 0) - це брехня(неістина)

# далі приклад перевірки, якщо є елементі в об'єкті
# те, що Python вважає пустий об'єкт брехнею дає нам спрощений запис без > 0, а просто назва об'єкта і все
# if len(l) > 0: # чи довжина об'єкта більше 0
#     pass
# if l: # чи об'єкт є True (бо якщо він пустий, то він буде False і умова не виконається)
#     pass

# is, is not - перевірка чи щось якляється чимось, або не являється чимось.
# !(порівняння саме по id об'єкта в пам'яті !не по значенню)
# l1 = [1,2,3]
# l2 = [1,2,3]
# l12 = l1
# print(f"{l1 is l2=}") # false
# print(f"{l1 is l12=}") # true
# print(f"{l2 is l12=}") # false
# print(f"{l2 is not l12=}") # true #!!! - IS перед NOT (бо в in буде навпаки)

# in - оператор, використовується до ітерабельних об'єктів - чи щось входить в щось, або не входить?
# in перевіряє по першому рівні вкладеності
# l = [1,2,3, [4,5], "test"]
# print(f"{1 in l =} # true
# print(f"{4 in l =}") # false (бо вона в середині ліста)
# print(f"{[4,5] in l =}") # true (є такий об'єкт повністю)
# print(f"{"t" in l =}") # false (в середину стрінги не стрибає - бере усю стрінгу для перевірки)
# print(f"{"test" in l =}") # true (ціла стрінга така є)
# працює для стрінги окремо теж
# print(f"{"es" in "test" =}")
# print(f"{"es" not in "test" =}") # NOT IN! not перед in
# для неітерабельних помилка
# print(f"{"es" not in 1 =}") #TypeError: argument of type 'int' is not iterable


# IF STATEMENT
# score = int(input("score:"))
# if score > 8:
#     print("start if true")
#     print("You have passed the exam")
#     print("end if true")

# print("Exam was finished.")


# temperature = float(input('What is the temperature? '))
# if temperature > 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
# print('Get some exercise outside.')


# є таке правило негласне - не заходити більше 2 або максимум 3 вкладень у блоці
# score = int(input("score:"))
# if score >= 90:
#     letter = 'A'
# else:
#     # grade must be B, C, D or F
#     if score >= 80:
#         letter = 'B'
#     else: # grade must be C, D or F
#         if score >= 70:
#             letter = 'C'
#         else: # grade must D or F
#             if score >= 60:
#                 letter = 'D'
#             else:
#                 if score >= 50:
#                     letter = 'E'
#                 else:
#                     letter = 'F'

# print(letter)


# првильніше написати ось таким чином через elif
# if score >= 90:
#     letter = 'A'
# elif score >= 80:
#     letter = 'B'
# elif score >= 70:
#     letter = 'C'
# elif score >= 60:
#     letter = 'D'
# elif score >= 50:
#     letter = 'E'
# else:
#     letter = 'F'

# print(letter)


# відповідь на питання, як знайти ліст в лісті 
# (рішення через перевірку типу, а далі вже працювати глибше, достукуючись до значень і яка стоїть задача)
# l = [1,2,3, [4,5], "test"]

# for i in l:
#     if type(i) is list:
#         print(i)


# ТЕРНАРНИЙ ОПЕРАТОР

# weather = "raining"

# if weather == "raining":
#     text = "Open Your umbrella" 
# else:
#     text = "Wear your cap"
# print(text) # !!! створена змінна в середині умови має доступ поза блоком (в python не мають доступ поза блоком (створюють власний скоуп) змінні створені в модулі, функції і класі)

# тернарний в Python
# text = "Open Your umbrella" if weather == "raining" else "Wear your cap"

# тернарний в інших мовах
# # text = weather == "raining" ? "Open Your umbrella" : "Wear your cap"
# print(text)


# MATCH CASE
# status = int(input("statuss code:"))

# match status: # службове слово match - що ми опрацьовуємо
#     case 400: # case - це умова
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 403  as code: # можна ставити умову для або | - тоді виконає якщо щось з них + можна через as створити тут додаткову змінну і використати далі в коді
#         print(f'{code} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# 
# # vj;tvj ds,eljdedfns wbkb gfnthys

# values = input("line:")
# values = values.split()
# print(f"{values =}")


# match values:
#     case "load", link: # якщо values це буде щось ітерабельне і на першому місці(на 0 індексі) буде стояти стрінг з текстом load -
# - і на другому місці є щось - збережи його в змінну link
#         print(link)
#     case "save", link, filename: # якщо values це буде щось ітерабельне і на першому місці(на 0 індексі) буде стояти стрінг з текстом save -
# - і складається з мінімум 3 елементів + на другому місці є щось - збережи його в змінну link, а третій - збережи в змінну filename
#         print("save")
#         print(f"\t{link}, {filename}")
#     case "save", link, *filenames: # якщо values це буде щось ітерабельне і на першому місці(на 0 індексі) буде стояти стрінг з текстом save -
# - і складається з мінімум 3 елементів + на другому місці є щось - збережи його в змінну link, а усе що далі збережи в змінну filename
#         print(f"save: {link}")
#         for filename in filenames:
#             print(f"\t{filename}")
#     case _: # дефолтне значення
#         print(values)

# коли є лісти і перебираємо за допомогою match case
t = (
    ["evening", "run"],
    ["all","sleep"],
    ["evening","party", "nothing"],
    ["night","party"],
    [1,2,3,4],
    "text",
)
for item in t:
    match item:
        case ['evening', action]:
            print(f'You almost finished the day! Now {action}!') # тут якщо є evening першим(індекс 0) і ліст із двох значень - то друге значення(індекс 1) записати в змінну
        case [time, action]: # якщо є ліст з 2 елементів, то взяти їх значення і присвоїти вказаним змінним
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid.')

# коли dict - структуру давати в match
# t = (
#     {"time":"evening", "action":"run"},
#     {"time":"evening", "action":"run", "city": "Lviv"},
#     {"time":"all", "action":"sleep"},
#     {"time":"all", "city": "Lviv"},
#     ["all","sleep"],
#     [1,2,3,4],
#     "text",
# )
# for item in t:
#     print(item, end=" => ")
#     match item:
#         case {"time": 'evening', "action": action}:
#             print(f'You almost finished the day! Now {action}!')
#         case {'time': time, 'action': action}:
#             print(f'Good {time}! It is time to {action}!')
#         case _:
#             print('The time is invalid.')

# як викручувались без match case раніше до 3.10 версії
# def f400():
#     print("Bad request")
# d = {
#     400: f400,
#     401: lambda : print("Unauthorized")
# }

# status = int(input("statuss code:"))
# try:
#     d[status]()
# except:
#     print("Other error")