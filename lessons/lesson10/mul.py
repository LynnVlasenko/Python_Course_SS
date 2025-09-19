# Множинне наслідування
#  в Пайтон можна наслідуватись від декількох класів, але більшість мов від такого підходу вже відмовились
#  воно підтримується, але практично не використовується - бо треба класно розуміти послідовність пошуку і перевіряти з mro
# zroj gj fh[bntrnehb ghjtrne gjnhb,yt vyj;syyt yfckbledfyyz - crjhbi pf dct yf gjxfnre погано продумали логіку]
# використовуватись може в реалізації інтерфейсу - то це просто реалізований клас який не має кнструктора, а просто набір методів, які мають бути і за цим принципом реалізовані
class A:
    def print_a(self):
        print("A")

class B:
    def print_b(self):
        print("B")

class C:
    def print_c(self):
        print("C")

class D(B, A):
    def print_d(self):
        print("D")
    def print_b(self):
        print("B from D")
        # або можна викликати від попереднього
    def old_print_b(self):
        super().print_b()
class E(C, A):
    def print_e(self):
        print("E")
    def print_b(self):
        print("B from E")
class F(D, E):
    def print_f(self):
        print("F")


f = F()

f.print_a()
f.print_b()
print(f.__dict__)
print(F.__dict__)
# для розуміння порядку, послідовності пошуку методів по класам - метод mro (метод резолюшн ордер)
print(F.mro())

print("===")
# в інтерпретованих мовах і в пайтон методи не копіюються(як в компільованих мовах)
# під час наслідування - до них надається доступ і коли нам потрібно достуватись і використати метод, то він його шукає за ключем і повертає функціональність як значення
# за рахунок цього пайтом повільніший, але в рази легший, бо не копіює постійно
print(A.__dict__)
print(B.__dict__)
print(C.__dict__)
print(D.__dict__)
print(E.__dict__)
print(F.__dict__)