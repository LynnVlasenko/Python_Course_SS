class User:
    count = 0

    def __init__(self, username, email):
        self.pk = self.get_total_users()
        self.username = username
        self.email = email
        User.count += 1

    def display_info(self):
        return f"ID: {self.pk}, Username: {self.username}, Email: {self.email}"

#  2 - методи класу (використання - метапрограмування??(коли треба модифікувати клас, збільшувати його) - розібратись)
# прийнято називати перший метод cls
# особливість - в незалежності від того - чи буде викликаний він від інстанса чи від класу - в обох випадках той об'єкт, який буде прилітати йому - це буде об'єкт класу
    @classmethod
    def get_total_users(cls):
        print(f"Class method called from {cls}")
        return cls.count
    
#  3 - статичні методи (прилетіли з інших мов програмування) - вони ні до інстанса ні до об'єкту класу не відноситься і його не отримує
# він є, але не використовується - краще просто створити звичайну функцію - як нижче (поза класом)
    # @staticmethod
    # def is_valid_email(email):
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     return re.match(pattern, email) is not None
    
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

users = [User("Alice", "alice@example.com"), User("Bob", "bob@example.com")]
print(users[0].display_info())
print(users[1].display_info())
print("Total users:", User.count)

# методи класу, які можуть існувати

#  1 - методи інстансу - метод, що описаний без жодного модифікатора (при виклику від інстанса - вони автоматично передають першим параметром інстанс)
# якщо виклик від об'єкту класу - то треба вказати параметр вручну в середині дужок
# print(User.display_info()) # This will raise an error because display_info requires an instance
print(User.display_info(users[0]))  # This works but is not a common practice

#  2 - методи класу
print(User.get_total_users())  # Correct way to call class method
print(users[0].get_total_users())  # This also works but is less common


# Інкапсуляція - доступ і закриття доступу до методів і аргументів класу (а пайтон це більше захис від дурака, бо усе одно є способи доступатись)
# в більшості мов програмування рівні захисту діляться на 3 рівні:
# публічні (name) - доступні всюди
# протектед (_name) - доступний в цьому об'єкті і класам нащадкам
# приватні (__name) - доступні тільки в цьому об'єкті (класам нащадкам - ні)


