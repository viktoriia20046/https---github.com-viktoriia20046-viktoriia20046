from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d') 

        # Отримуємо поточну дату
        current_date = datetime.today()

        # Розраховуємо різницю між поточною датою та заданою датою
        difference = input_date - current_date

        # Повертаємо різницю у днях як ціле число
        return difference.days 
    except ValueError:
        # Обробляємо виняток, якщо вхідні дані мають неправильний формат
        print("Неправильний формат дати. Використовуйте '%Y-%m-%d' ")
        return None

# Отримуємо поточну дату та форматуємо її до 'РРРР-ММ-ДД'
today = datetime.today().strftime('%Y-%m-%d')

# Викликаємо функцію з прикладом дати '2021-06-29'
result = get_days_from_today('2021-06-29')

# Виводимо результат
print(f"Сьогодні {today}, кількість днів до 2021-06-29: {result}")

#Завдання 2 

import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка валідності вхідних даних
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        return []

    # Генерація унікальних чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        random_number = random.randint(minimum, maximum)
        numbers_set.add(random_number)

    # Перетворення множини в список та сортування
    sorted_numbers = sorted(list(numbers_set))
    return sorted_numbers

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

#Завдання 3
import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Перевірка чи номер починається з '+'
    if cleaned_number.startswith('+'):
        return cleaned_number
    else:
        # Додаємо міжнародний код '+38'
        return '+38' + cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#4 завдання 
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначення дати народження на наступний рік, якщо вона вже минула у поточному році
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Визначення різниці між днем народження та поточним днем
        days_until_birthday = (birthday - today).days

        # Перевірка, чи день народження випадає вперед на 7 днів
        if 0 <= days_until_birthday <= 7:
            # Перенесення дати привітання на наступний понеділок, якщо день народження припадає на вихідний
            if birthday.weekday() in [5, 6]:
                next_monday = birthday + timedelta(days=(7 - birthday.weekday()))
                congratulation_date = next_monday.strftime("%Y.%m.%d")
            else:
                congratulation_date = birthday.strftime("%Y.%m.%d")

            # Додавання інформації до списку привітань
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
