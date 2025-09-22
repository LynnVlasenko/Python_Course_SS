import os

from dotenv import load_dotenv #для зберігання ключів (створили файл з крапкою - де зберегли ключ і в коді тоді прописали просто назву змінної)
from pyowm import OWM


load_dotenv()  # take environment variables - тут якщо називаємо файл інакше ніж .env (це за описом до бібліотеки https://pypi.org/project/python-dotenv/) - то в дужках пишемо - .ім'я
#для зберігання ключів (створили файл з крапкою - де зберегли ключ і в коді тоді прописали просто назву змінної) - той файл буде в гіт ігнорі і його не побачать
API_KEY = os.getenv("API_KEY")

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# city = "Lviv,UA"
city = input("Enter city name: ")

obs = mgr.weather_at_place(city)
w = obs.weather

weather_info = {
    "Status": w.detailed_status,
    "Wind": w.wind(),
    "Humidity": w.humidity,
    "Temperature": w.temperature('celsius'),
    "Rain": w.rain,
    "Heat Index": w.heat_index,
    "Clouds": w.clouds,
}
from pprint import pprint
pprint(weather_info)