# Колекції - термін пішов з C++. ітерабельні обяєкти, що зберігають набір даних.

# Впорядковані колекції - list(changeable), tuple(unchangeable)
# Не впорядковані - set(не має дублікатів), dict(він в якомусь сенсі ордеред, але по-інакшому)(не має дублікатів по ключах)

# list

# Основні способи створити list:
# 1:
# l = list()
# print(type(l), l) # поверне об'єкт class 'list' []

# 2: Створення з передачею значень (Приймає лише 1 об'єкт, має бути ітерабельний)
# # l = list(1, 2, 3)#TypeError: list expected at most 1 argument, got 3
# # l = list(1) #TypeError: 'int' object is not iterable
# l = list([1, 2, 3])
# print(type(l), l) # поверне об'єкт class 'list' [1, 2, 3]
# l = list("text") 
# print(type(l), l) # поверне об'єкт class 'list' ['t', 'e', 'x', 't']

# 3: основний спосіб (найчастіше використовується) - пприсвоєння[]
# l = []
# print(type(l), l)
# l = [1, "text", 2.5, [1,23], (1, 2)]
# print(type(l), l)

# ДОСТУП ДО ЕЛЕМЕНТІВ
# доступ за індексом по верхній вкладеності,
# l = [1, "text", 2.5, [1,23], (1, 2)]
# print(l[0])
# print(l[1][1]) # доступ до елементу вкладеного ліста
# print(l[2])
# print(l[3], l[3][0], l[3][1])
# print(l[4])

# додавання референсу на сомого себе 
# (в list додасться посилання на цей сами ліст і це буде виглядати як [...])
# l.append(l) 
# print(l)
# доступ до посилання на самого себе - можна безкінечно там по колу звертатись до останнього об'єкту який є посиланням на самого себе а в середині нього ж так само в кінці посилання на себе і це безкінечність.
# print(f"{l[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1]} =")

# ЗАМІНА ЗНАЧЕННЯ ЗА ІНДЕКСОМ (UPDATING)
# l[0] = 100
# print(l) 

# SLICING
# print(l[1:5]) # вибере значення по індексах і обрізає по ним список
# print(l[2::2]) # з 2 до кінця з кроком 2
# print(l[::]) # дефолтно від початку (0 індекс) до кінця (n-1 індекс) з кроком 1
# print(l[2:2]) # пустий буде - бо на місці залишився
# print(l[::-1]) # поверне обернений список

# ДОДАВАННЯ (конкатенація) list-ів
# print([1,2,3]+[4,5,6])

# МНОЖЕННЯ (repetition) list-ів
# print([1,2,3]*3)

# ПЕРЕВІРКА НАЯВНОСТІ ЕЛЕМЕНТА В LISTі (MEMBERSHIP)
# перевіряє у верхній вкладеності
# l = [1, "text", 2.5, [1,23], (1, 2)]
# print(f'{1 in l=}') # true
# print(f'{"text" in l=}') # true
# print(f'{"t" in l=}') # false
# print(f'{"t" in l[1]=}') # true (так можемо перевірити в вкладеному ітерабельному об'єкті)
# print(f'{2.5 in l=}') # true
# print(f'{[1,23] in l=}') # true
# print(f'{(1, 2) in l=}') # true

# ПОРІВНЯННЯ (Comparison)
# print([1,2,3] == [1,2,3]) # true
# print([1,2,3] == [1,3,2]) # false
# print([1,2,3] == [1,2,4]) # false
# print([1,2,3] == [1,2,3,4]) # false
# print([1,2,3] == (1,2,3)) # false


# МЕТОДИ LISTа

# print([method for method in dir(list) if not method.startswith("__")])
# a = []

# ДОДАВАННЯ НОВОГО ЕЛЕМЕНТУ В LIST
# append - приймає в себе об'єкт і додає його в кінець списку
# a.append(1)
# a.append("text")
# a.append("text")
# a.append([1, 2, 3])
# print(a)

# РОЗШИРЕННЯ list-a
# extend - приймає ітерабельний об'єкт і додає елементи цього об'єкти в список поелементно
# a.extend([4, 5, 6])
# print(a)

# ВСТАВЛЕННЯ ЕЛЕМЕНТА
# insert - приймає два переметра (індекс (куди вставити) і значення(що вставити))
# після вставлення, елемент, який був на цьому індексі, здвигається далі і стає наступним по рахунку, відповідно усі наступні елементи теж змінюють свій індекс на +1.
# a.insert(1, "inserted")
# print(a)

# ВИДАЛЕННЯ ЕЛЕМЕНТІВ (remove, pop)
# remove - приймає в себе параметр(значення), яке ми хочемо видалити зі списку 
# - і видалить його перше входження у списку (значення має бути у списку, якщо ні - помилка)
# - і нічого не повертає (None)
# result = a.remove("text")
# # a.remove("1text") #ValueError: list.remove(x): x not in list
# print(result, a)

# pop - видаляє останній елемент у списку
# - і повертає значення яке видалив
# - може приймати параметр - індекс - і видаляти значення за індексом і повертає видалене значення
# result = a.pop()
# print(result, a)
# result = a.pop(0)
# print(result, a)

# ПОШУК ІНДЕКСА ЗА ЗНАЧЕННЯМ
# index - приймає значення і повертає індекс цього значення (бере перше входження у списку)
# - приймає другий параметр - індекс з якого почати шукати
# - приймає третій параметр - індекс до якого шукати
# - якщо такого знаяення немає в списку = помилка
# a = [1,2,3,4,1,2,3,4,5,1,2,3,4, "text", "text", [1, 2, 3]]
# print(a)
# i = a.index(1)
# print(i)
# i = a.index(1, i + 1)
# print(i)
# i = a.index(1, len(a) - 1)#ValueError: 1 is not in list
# i = a.index(1, i + 1)
# print(i)
# i = a.index(1, i + 1, 8)

# ПОШУК КІЛЬКОСТІ ОБ'ЄКТІВ, ЕЛЕМЕНТІВ В СПИСКУ
# count - приймає значення/об'єкт і рахує кількість входжень цього значення/об'єкта у списку - повертає int
# print(a.count(1)) # 3
# print(a.count("text"))
# print(a.count([1,2,3]))


# ЧИЩЕННЯ ЗНАЧЕНЬ У СПИСКУ
# clear - чистись усі знаяення у списку, залишаючи об'єкт списку порожнім, але не видаляє сам об'єкт і посилання на нього
# a = [1,2,3]
# print(id(a), a)
# a.clear()
# print(id(a), a)

# Приклад з чищенням і створенням просто нового об'єкту
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9, a, b]
# print(c)
# print(id(c[3]) == id(a)) # true
# print(c[4] is b) # true
# a.clear() # залишить посилання на об'єкт
# b = [] # перезапише посилання на об'єкт
# print(a, b)
# print(c) # поверне [7,8,9, [], [4,5,6]] # бо тут передається посилання першого b
# print(id(c[3]) == id(a)) # true
# print(c[4] is b) # false


# КОПІЮВАННЯ ЗНАЧЕНЬ У СПИСКУ
# copy:
# shallow copy - (базове копіювання) - копіює референс на об'єкт, якщо він mutable. (immutable - копіює значення)
# deep copy - (можливо лише з додатковими бібліотеками (import copy / copy.deepcopy())) - створює повністю новий об'єкт і переносить усі значення в нього з новими посиланнями
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9, a, b]
# d = c.copy() # поверне значення (нові створені об'єкти для 7,8,9, і посилання на a, b)
# print(c, d)
# a[0] = 100
# c[0] = 200
# c[3][2] = 300
# print(a, b)
# print(c)
# print(d)
# import copy
# dd = copy.deepcopy(c)
# print(c, d)
# a[0] = 99
# c[0] = 85
# c[3][2] = 73
# print(a, b)
# print(c)
# print(d)
# print(dd)

# способи скопіювати list
# v = list(c)
# # v.copy(c)
# print(f"v = {v}")
# w = copy.copy(c)
# print(f"w = {w}")

# ВПОРЯДКУВАННЯ ЗНАЧЕНЬ У СПИСКУ
# reverse - розвертає список у зворотньому порядку
# l = [1,2,4,2,3,5,7,8,43,3,21]
# print(l)
# l.reverse()
# print(l)

# reversed() - створює список у зворотньому порядку - з новим на нього посиланням (не модифікує оригінальний)

# sort - сортує список по зростанню (модифікуючи оригінальний список)
# (!сортує лише елементи одного типу, якщо у списку різні = помилка)
# - можна обійти таку поведінку через lambda (# l.sort(key=lambda x: str(x)))
# l.sort()
# print(l)
# l = [1, "a5",2,"4",]
# # l.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
# l.sort(key=lambda x: str(x))  # Sorts by string representation
# print(l)

# sorted() - повертає відсортовану копію об'єкта - з новим на нього посиланням (не модифікує оригінальний)
# a = [1,3,1,5,2,4]
# print(sorted(a))  # Returns a new sorted list
# print(a)  # Original list remains unchanged


# BUILT-IN FUNCTIONS
# all() - приймає в себе щось ітерабельне і поверне true, якщо усі елементи є true (або, якщо список пустий), якщо хоч один false, повернк false
y = [1, 0]
all(y)
# any() - приймає в себе щось ітерабельне і поверне false, якщо усі елементи є false, і true якщо хоч один true
y = [0, 0]
any(y)
# enumerate() - приймає список і розкладає його на список тюплів з індексом і значенням списку.
# len() - повертає довжину списку
# list() - створює об'єкт ліста, або перетворює в ліст інший ітерабельний об'єкт
# max() - повертає максимальне значення у списку
# min() - повертає мінімальне значення у списку
# sorted() - повертає відсортовану копію об'єкта - з новим на нього посиланням (не модифікує оригінальний)
# sum() - сумує значення у списку


# LIST COMPREHENSION: Elegant way to create a new list
# використовують для простих кейсів, або коли треба швидкість виконання (запис у COMPREHENSION буде швидший за цикл, бо буде на ходу створювати ліст)
# присвоюється до змінної у квадратних дужках, де будемо створювати список
# в середині дужок пишемо чим наповнюємо елементи(expression), з відки беремо їх(for value in collection) і яка умова (if condition)
# це по факту такий запис як звичайно ми пишемо цикл for і робимо append список (і в ньому чи є чи нема умови) - просто це в іншому форматі записано і буде створювати список на ходу

# matrix = [[i, j] for i in range(3) for j in range(3) if i != j]
# print(matrix)

# matrix = []
# for i in range(3):
#     for j in range(3):
#         if i != j:
#             matrix.append([i, j])

# ---------------------------------------------------------------------------------------

# TUPLE
# ОСОБЛИВОСТІ:
# 1 - створрюється у звичайних дужках, і не є змінюваним (по факту ліст, але unmutable)
# 2 - коли створюємо тюпл з 1 елементом, або знаємо що прийде лише 1 елемент спочатку (робити перевірку)
# - то треба поставити кому після 1 елементу, щоб було зрозуміло, що це tuple, а не просто значення в дужках, визначений як пріорітетний
# 3 - tuple буде займати менше місця ніх list
# 4 - результатом tuple COMPREHENSION буде генератор

# Cтворення схожі як і в ліст
# t = tuple()
# print(type(t), t)
# t = tuple([1, 2, 3])
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = (1,2,3)
# print(type(t), t)
# t = (1)
# print(type(t), t)
# t = (1,)
# print(type(t), t)


# МЕТОДИ TUPLE
# так як tuple не можна модифікувати, він має всього 2 методи: index, count (працють як і з list)
# print([method for method in dir(tuple) if not method.startswith("__")])

# ДОСТУП ДО ЕЛЕМЕНТІВ
# доступ за індексом по верхній вкладеності,
# t = (1, 2, 3, [4, 5, 6])
# print(t)
# print(t[0])
# print(t[3])

# ЗАМІНА ЗНАЧЕННЯ ЗА ІНДЕКСОМ (UPDATING) - !НЕ ПРАЦЮВАТИМЕ, ТАК ЯК UNMUTABLE
# # t[0] = 100 # TypeError: 'tuple' object does not support item assignment
# - але, якщо в середині тюпла є ліст, то в тому лісті модифікувати можна(але поміняти референс на ліст - ні):
# t[3][0] = 100  # This is allowed because the list inside the tuple is mutable
# print(t)

# результатом tuple COMPREHENSION буде генератор - 
# приклад поведінки tuple і list, при COMPREHENSION:

# for n in range(1,10):
#     print(f"{n=}")
#     l = [e for e in range(n**2)]
#     t = (e for e in range(n))
#     print(f"\t{l.__sizeof__()=} {l[:15]=}")  # повертає lіst 
#     print(f"\t{t.__sizeof__()=} {t=}") # повертає об'єкт генератора 
# за розміром tuple буде завжди однаковий, бо генератор поелементно віддає і зберігає розмір лише свого функціоналу для розрахунку
# а list буде дуже сильно рости


# BUILT-IN FUNCTIONS (такі як в list - вище описано)


# ---------------------------------------------------------------------------------------
#SET
# set - це множини - взяті напряму з математики
# ОСОБЛИВОСТІ:
# 1 - не створює дублікати (коли намагаємось додати елемент, який вже є - він просто його не додасть, або якщо від початки пишемо set([1, 2, 3, 1, 3, 2, 1]) - отримаємо {1, 2, 3})
# - унікальність визначає за хешом - у кожного елемента буде свій унікальний хеш - визначити можна методом s.__hash__
# 2 - повертає НЕ впорядкований список (елементи кожного разу будуть у різній послідовності і немає логіки як саме вони розкидані - просто рандомно)
# 3 - в set можна зберігати лише хешбл об'єкти(з яких можна дістати хеш - функція, яка вираховує унікальність об'єкту (бере об'єкт і вираховує його у число - на один і той самий об'єкт, буде один і той самий хеш)) 
# (unhashable є list) - чому? (якщо перейти в клас list - то метод hesh там просто заборонений - вказаний в ручну як None))) насправді усі об'єкти повертаються hashable.
# 4 - не можна створити set через {} - це поверне dict. Тобто пустий set створюємо лише через ім'я класу set() або треба встатити хоча б 1 елемент, щоб інерпретатор розумів, що в наповненні це set.


# СТВОРЕННЯ
# s = set()
# print(type(s), s)
# s = set([1, 2, 3, 1, 3, 2, 1])
# print(type(s), s)
# s = set("dshbfhsdvhgsafdhgsafdhgsafdhgsafdhgds")
# print(type(s), s)
# s = {}
# print(type(s), s)
# s = {1,2,1,2,1,2}
# print(type(s), s)


# МЕТОДИ SET
# print([method for method in dir(set) if not method.startswith("__")])

# add - додати елемент в set
# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(3) # другу 3 не додасть (помилки не буле - просто не додасть)
# print(s)

# clear - працює як в list (опис вище)
# copy - працює як в list (опис вище)

# pop - видаляє рандомно елемент з set і повертає його значення (!параметри в себе не приймає)
# print(s.pop())

# remove - приймає елемент і пробує його видалити, якщо такого значення в set нема - ерор
# print(s.remove(2)) 
# print(s)

# update - як extend в list - бере щось ітерабельне і поелементно додає в сет значення
# print(s.update([1,2,3]))
# print(s)
# print(set("hsdfhdsbfjbgfdbghbsdbgjk"))


# МЕТОДИ SET - для пошуку унікальних або сумісних значень
# результатом цих методів буде - створений новий set

# це як кола Ейлера - з математики з теорії множин
# set має свої методи для цих задач:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union() - повертає об'єднані два set-a (усі значення обох (повторювані в різних сетах значення запише 1 раз))
print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A)) # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection() - перетин (які значення є в обох set-aх)
print(A & B) # {4, 5}
print(A.intersection(B)) # {4, 5}
print(B.intersection(A)) # {4, 5}

# differense() - покаже різницю одного сета по відношенню до іншого (які елементи є в цьому сеті і немає в порівнюваному))
print(A - B) # {1, 2, 3} # в А є {1, 2, 3}, а в В таких немає
print(B - A) # {6, 7, 8} # в В є {6, 7, 8}, а в А таких немає
print(A.intersection(B)) # {1, 2, 3}
print(B.intersection(A)) # {6, 7, 8}

# symmetric_difference() - поверне лише унікальні(не спільні) значення сетів по відношенню один до одного (значення, ті що були присутні в обох сетах прибере) (по факу як сума differense для обох set-ів)
print(A ^ B) # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B)) # {1, 2, 3, 6, 7, 8}
print(B.symmetric_difference(A)) # {1, 2, 3, 6, 7, 8}

# isdisjoint() - перевіряє, чи множини не мають спільних елементів.
# Якщо перетину немає → повертає True.
# Якщо хоч один спільний елемент є → False.
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

print(a.isdisjoint(b))  # True (немає спільних)
print(a.isdisjoint(c))  # False (спільний елемент 3)

# issubset() - перевіряє, чи усі елементи множини містяться в іншій множині.
# Якщо a є підмножиною b → True.
# Інакше → False.
a = {1, 2}
b = {1, 2, 3, 4}

print(a <= b)   # True
print(a.issubset(b))   # True (усі з a є в b)
print(b.issubset(a))   # False

# issuperset() - протилежний до issubset(). (перевіряє в іншу сторону)
# Перевіряє, чи множина містить усі елементи іншої множини.
a = {1, 2, 3, 4}
b = {2, 3}

print(a >= b)  # True
print(a.issuperset(b))  # True (a включає b)
print(b.issuperset(a))  # False


# BUILT-IN FUNCTIONS (такі як в list - вище описано)
# enumerate() -  в set дасть індекси, але кожного разу дає різні значення під індекси - то можливо для якоїсь одноразової задачки, якщо треба можна використати, 
# !але пам'ятати, що значення під індексами на наступний запуск зміняться.
# sorted - поверне відcортований list


# ---------------------------------------------------------------------------------------
# FROZENSET
# усе те саме що і для set але frozenset є unmutable.
# - тому він має лише такі методи copy(), differense(), intersection(), symmetric_difference(), union()
#  - а також isdisjoint(), issubset(), issuperset()


# ---------------------------------------------------------------------------------------
# DICT

# dict - самий основний тип в python - бо усі об'єкти є діктоподібними.
# ОСОБЛИВОСТІ:
# 1 - ключем може бути лише хешбл об'єкт


# СТВОРЕННЯ:
# d = dict()
# print(type(d), d)
# d  = dict([(1, 'a'), (2, 'b'), (3, 'c')]) # такий спосіб можливий, але рідко використовуваний
# # d  = dict([(1, 'a'), (2, 'b'), (3, 'c', 3)])#ValueError: dictionary update sequence element #2 has length 3; 2 is required
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     11: 'a',
#     "2": 'b',
#     (22, 3): 'c'
# }
# print(type(d), d)


# ДОСТУП ДО ЕЛЕМЕНТІВ
# доступ до значення за ключем
# print(d[11])
# print(d["2"])
# print(d[(22, 3)])

# ДОДАВАННЯ ЕЛЕМЕНТУ:
# прописали новий ключ і присвоїли значення
# d["42424"] = 12 

# ЗАМІНА ЗНАЧЕННЯ ЗА КЛЮЧЕМ (UPDATING)
# d[11] = 13
# print(d)

# доступ до неіснуючого ключа - помилка
# d["text"] #KeyError: 'text'


# МЕТОДИ DICT
# print([method for method in dir(dict) if not method.startswith("__")])

# d = {
#     11: 'a',
#     "2": 'b',
#     (22, 3): 'c'
# }

# clear, copy - працюють як в list (опис вище)

# get - знаходить значення за ключем (! є безпечним методом - якщо вказується неправильний ключ - поверне None, а не дасть помилку)
# - можна вказувати другий параметр, який повернеться, якщо такого ключа не існуватиме в set
# print(d.get(11))
# print(d.get("text"))
# print(d.get(11, 100))
# print(d.get("text", 100))

# pop - видаляє значення за ключем (!параметр ключа обов'язковий / без переметру - ерор)
# - теж можна вказувати другий параметр, який повернеться, якщо такого ключа не існуватиме в set
# - поверне значення видаленого елементу
# print(d.pop(11))
# print(d.pop(11, 100))  # Returns 100 if key 11 is not found

# popitem() - повертає пару (ключ, значення) останнього доданого в словник елемента
# - останній елемент в dict - це (з версії 3,6 (коли додали ордерінг по часу додавання елемента в dic - від найстарішого до наймолодшого) - останній доданий в словник елемент (до цього був як set - рандомно формувався))
# print(d.popitem())  # Returns 100 if key 11 is not found
# print(d)

# update - як extend в list - бере тип dict (ключі і значення) і додає їх в dict, до якого викликається, поелементно.
# d.update({1: "one", 2: "two"})
# print(d)

# методи для побудови алгоритмів більше keys, values і items
# keys - поверне list з усіма ключами
# values - поверне list з усіма значеннями
# items - поверне list з усіма ключами і значеннями у вигляді tuples [(ключ, значення)]
# print(d.keys())
# print(d.values())
# print(d.items())

# коли ми перебираємо dict - перебір йде по ключах і потім ми пожемо дістати значення
# але, використовуюся items() ми можемо відразу звертатись і до ключів і до значень:
# for key in d:
#     print(f"{key} -> {d[key]}")

# a,b = (2,3)
# print(a, b)

# for key, value in d.items():
#     print(f"{key} -> {value}")

# fromkeys - метод, що прилетів з пайтона 2
# приймає list з ключами і значення (тобто fromkeys([1, 2, 3], "default") - це створить три елемента з ключами 1, 2, 3 і надасть їм значення "default")
# - і повертає новий список
# - але виходить, що він працює лише коли його використовувати на якомусь dict, але по факту цей dict не приймає участі в створенні нового dict-a
# - тому можна просто викликати з dict # dd = dict.fromkeys([1, 2, 3], "default")
# - тобто зробили його не тільки від клас методом, але і від інстанс методом
# dd = d.fromkeys([1, 2, 3], "default")
# print(dd)

# setdefault - приймає значення ключа і повертає значення за цим ключем 
# - працює як get, якщо переданий ключ існує в словнику - тобто просто поверне значення за ключем
# - але, якщо ключ не існує, то setdefault розширить словник, додаючи цей ключ у словник і присвоїть йому значення None
# - також можна передавати другий параметр, який буде присвоєно новому ключу, ЯКЩО ЙОГО НЕ БУДЕ ЗНАЙДЕНО У СЛОВНИКУ

# dict.setdefault(key, default=None)
# key – ключ, який ми хочемо отримати.
# default – значення, яке буде додане, якщо ключа немає (за замовчуванням None).

# Як працює:
# Якщо ключ є у словнику → повертається його значення.
# Якщо ключа немає → ключ додається у словник зі значенням default, і це значення повертається.

# Приклад:
# person = {"name": "Alina", "age": 25}

# # ключ "age" існує
# print(person.setdefault("age", 30))   # 25
# print(person)  # {"name": "Alina", "age": 25}

# # ключ "city" не існує
# print(person.setdefault("city", "Kyiv"))  # "Kyiv"
# print(person)  # {"name": "Alina", "age": 25, "city": "Kyiv"}
# 🔹 Використання
# Метод зручний, коли потрібно:
# уникнути помилки KeyError, якщо ключа немає;
# додати значення за замовчуванням для нового ключа.

# Різниця між setdefault() і get():
# get(key, default) тільки повертає значення (не змінює словник).
# setdefault(key, default) може створити новий ключ у словнику.


# BUILT-IN FUNCTIONS
# all() - по ключах перевіряє, 
# any() - по ключах перевіряє, 
# len() 
# i sorted()

# sorted - працює лише з доповненням lambda (так як ключі можуть бути різних типів, спочатку привести їх до стрінги, або вказати свій спосіб сортування у функцію, який потрібний)
# sorted_dict = dict(sorted(d.items(), key=lambda item: str(item[0])))
# print(sorted_dict)



# Create a list of integers that are entered from the terminal 
# and determine the maximum and minimum number among them.

# numbers = []
# while True:
#     numbers_input = input("Enter an integer or 'done' to finish: ")
#     if numbers_input == "done":
#         break
#     try:
#         number = int(numbers_input)
#         numbers.append(number)
#     except ValueError:
#         print("Invalid input. Please enter an integer or 'done'.")

# if numbers:
#     maximum = max(numbers)
#     minimum = min(numbers)
#     print(f"The maximum number is: {maximum}")
#     print(f"The minimum number is: {minimum}")
# else:
#     print("No numbers were entered.")


# Task1. In the range from 1 to 10 determine 
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

# even_divisible_by_2 = []
# odd_divisible_by_3 = []
# not_divisible_by_2_or_3 = []

# for number in range(1, 11):
#     if number % 2 == 0:
#         even_divisible_by_2.append(number)
#     if number % 2 != 0 and number % 3 == 0:
#         odd_divisible_by_3.append(number)
#     if number % 2 != 0 and number % 3 != 0:
#         not_divisible_by_2_or_3.append(number)

# print(f"Even numbers divisible by 2: {even_divisible_by_2}")
# print(f"Odd numbers divisible by 3: {odd_divisible_by_3}")
# print(f"Numbers not divisible by 2 and 3: {not_divisible_by_2_or_3}")


# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. 
# If the login is different, send an error message.
# (need to use loop while)

# while True:
#     login = input("Enter your login: ")
#     if login == "First":
#         print("Hello!")
#         break
#     else:
#         print("Error: Incorrect login.")


