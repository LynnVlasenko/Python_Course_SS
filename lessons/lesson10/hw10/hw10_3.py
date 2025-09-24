# Create a class "BankAccount" that implements encapsulation. The class should have the following attributes:

# account_number (string)
# account_holder (string)
# balance (float)
# The class should have the following methods:

# deposit(amount) - a method that allows the account holder to deposit money into the account
# withdraw(amount) - a method that allows the account holder to withdraw money from the account; write "Insufficient funds" if money doesn't enough
# check_balance() - a method that returns the current balance of the account
# The class should also have the following restrictions:

# account_number should not be accessible from outside the class
# balance should not be directly accessible from outside the class, it should only be accessible through the methods deposit() and withdraw()
# account_holder should be accessible from outside the class but should not be modifiable

class BankAccount:

    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    
    @property
    def account_holder(self):
        return self.__account_holder
    
    @account_holder.setter
    def account_holder(self, value):
        try:
            raise AttributeError("Sorry! You can't modify account holder name")
        except AttributeError as e:
            print(f"Warning! -> {e}")

    def deposit(self, amount: float):
        self.__balance += amount
        return f"You put {amount} on your card, now your balance is {self.__balance}"
    
    def withdraw(self, amount: float):
        if (self.__balance - amount) <= 0:
            return "Insufficient funds"
        else:
            self.__balance -= amount
            return f"You have withdrawn {amount} from your card, now your balance is {self.__balance}"
    
    def check_balance(self):
        return self.__balance


ac = BankAccount("A4567", "Lynn Vlasenko", 5672.78)

ac.account_holder = "Alina" # AttributeError: property 'account_holder' of 'BankAccount' object has no setter
print(ac.account_holder)
print(ac.check_balance())
print(ac.deposit(345.7))
print(ac.withdraw(18.48))


# Create a program that models a zoo. The program should have a base class Animal 
# that stores the animal's name, species, and number of legs. 
# The class should have a method make_sound that returns a string indicating the sound the animal makes. 
# The make_sound method should be overriden in the subclasses to return a sound specific to each type of animal.

# Then, create three subclasses of Animal: Mammal, Bird, and Reptile. 
# Each of these subclasses should inherit the name, species, and number of legs from the Animal class.

# For the Mammal class, add a method give_birth and return "Roar" for make_sound method.

# For the Bird class, add a method lay_eggs and return "Squawk" for make_sound method.

# For the Reptile class, add a method shed_skin and return "Hiss" for make_sound method.


# 🔹 Що таке абстрактний клас?

# Абстрактний клас — це клас, який не можна створювати напряму (не можна зробити animal = Animal()), бо він задуманий як "шаблон".

# Він містить абстрактні методи, які підкласи обов’язково мають перевизначити.

# 🔹 Що таке абстрактний метод?

# Це метод, який існує у базовому класі, але не має реалізації.

# Він тільки каже: "Кожен, хто наслідується від мене, мусить це реалізувати".

# У Python це робиться через модуль abc (Abstract Base Classes).
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__ (self, name: str, species: str, number_of_legs: int):
        self.name = name
        self.species = species
        self.number_of_legs = number_of_legs
    
    @abstractmethod
    def make_sound(self):
        pass

# Animal тепер абстрактний.
# Якщо ти спробуєш зробити a = Animal("Bob", "Unknown", 4) → отримаєш помилку TypeError: Can't instantiate abstract class.

# Тепер у підкласах ти змушена реалізувати make_sound:
# Якщо ти забудеш реалізувати make_sound у підкласі → Python теж видасть помилку при створенні екземпляра.

# Навіщо це потрібно?
# Це гарантує, що всі підкласи будуть мати однаковий інтерфейс (у нашому випадку метод make_sound).
# Код стає більш надійним: інші програмісти, які пишуть підкласи, не зможуть "забути" реалізувати потрібний метод.
# Це часто використовується в бібліотеках і фреймворках, щоб задати правила, як треба наслідувати класи.

class Mammal(Animal):
    # def __init__ (self, name: str, species: str, number_of_legs: int):
    #     super().__init__(name, species, number_of_legs)
    #     self.name = name
    #     self.species = species
    #     self.number_of_legs = number_of_legs

    def give_birth(self):
        pass

    def make_sound(self):
        return "Roar"

m = Mammal("dfdf", "sddff", 4)
print(m.make_sound())
    
class Bird(Animal):
    # def __init__ (self, name: str, species: str, number_of_legs: int):
    #     super().__init__(name, species, number_of_legs)
    #     self.name = name
    #     self.species = species
    #     self.number_of_legs = number_of_legs

    # переписування ініту потрібне лише коли додаються нові аргументи - тоді використовуємо super для базових батьківських
    # без додавання нових базові автоматично днадаються під час наслідування
    def __init__(self, name: str, species: str, legs: int, can_fly: bool = True):
        super().__init__(name, species, legs)  # ініціалізує базові поля
        self.can_fly = can_fly                 # додає нове поле

    def lay_eggs(self):
        pass

    def make_sound(self):
        return "Squawk"

class Reptile(Animal):
    # def __init__ (self, name: str, species: str, number_of_legs: int):
    #     super().__init__(name, species, number_of_legs)
    #     self.name = name
    #     self.species = species
    #     self.number_of_legs = number_of_legs
    
    def shed_skin(self):
        pass

    def make_sound(self):
        return "Hiss"