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