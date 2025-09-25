# Логування в пайтон
# потрібно імпортувати модуль logging
# логування прописують на певні дії, які потрібно відслідковувати для розуміння подій у програмі і аналізу виникнення помилок - їх відтворення.

import logging

# його можна конфігурувати (дефолтно level=logging.WARNING буде)
# level з якого рівня виводити логи,  (можна прописувати функцію, яка дозволяє переключати рівні і якщо не треба бачити інфо, а лише від помилок починаючи - то собі переключати і робити це на ходу, не зупиняючи логування як таке)
# format - в якому форматі виводити меседж - в нас буде час видно виведення, який рівень, назву функції де залогувало щось і повідомлення
# до форматів є табличка і там багато можна писати налаштувань docs.python.org/3/library/logging.html
# datefmt - модифікатор дати
# filename - створить файл куди зберігати і буде туди записувати логи
# filemode - (будемо ще по файлам розбирати) - mode 'а' - говорить, що "дозаписуй файл"(не переписуй), 'w' - це перезапис
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app.log',
                    filemode='a'
                    )
# logger = logging.getLogger(__name__)

# рівні логування - вони мають свою послідовність
# якщо ми в конфігуруванні виставимо рівень(level) певний, то будуть виводитись лише ті, що виставили і нижче - вище не буде видно
# числа прописані в коментарях навпроти - це реальні чфисла з налаштувань, якщо перейти через command по методу вище - де logging.ERROR - то видно
logging.debug('This is a debug message') # 10
logging.info('This is an info message') # 20
logging.warning('This is a warning message') # 30
logging.error('This is an error message') # 40
logging.critical('This is a critical message') # 50


# приклад як використовувати у функції:
# коли маємо помилку - то записуємо її в логер - запис такого формату з методом помилки logging.error("Attempted to divide by zero", exc_info=True)
# а якщо помилки нема - то інформуй, що усе ок - logging.info("Division successful")
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero", exc_info=True)
        return None
    else:
        logging.info("Division successful")
        return result
    
if __name__ == "__main__":
    divide(10, 2)
    divide(10, 0)

# багато різних конфігурацій є для логів - можна конфігурити під кожен процес якийсь окремо файл (для модулів для пекеджів)
# можна налаштовувати по часу на кожен день новий файлик