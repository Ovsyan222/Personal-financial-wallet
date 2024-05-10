import json
import os

# Файл для хранения данных
data_file = "finances.json"

# Проверка существования файла и чтение данных
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        data = json.load(file)
else:
    data = []

def save_data():
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def show_balance():
    total_income = sum(record['amount'] for record in data if record['category'] == 'Доход')
    total_expense = sum(record['amount'] for record in data if record['category'] == 'Расход')
    total_balance = total_income - total_expense

    print(f"Текущий баланс: {total_balance} руб.")
    print(f"Доходы: {total_income} руб.")
    print(f"Расходы: {total_expense} руб.")

def add_record():
    record = {}
    record['date'] = input("Введите дату (гггг-мм-дд): ")
    record['category'] = input("Введите категорию (Доход/Расход): ")
    record['amount'] = float(input("Введите сумму: "))
    record['description'] = input("Введите описание: ")

    data.append(record)
    save_data()
    print("Запись успешно добавлена.")

def edit_record():
    date_to_edit = input("Введите дату записи для редактирования (гггг-мм-дд): ")

    for record in data:
        if record['date'] == date_to_edit:
            record['category'] = input("Введите новую категорию (Доход/Расход): ")
            record['amount'] = float(input("Введите новую сумму: "))
            record['description'] = input("Введите новое описание: ")
            save_data()
            print("Запись успешно отредактирована.")
            return

    print("Запись не найдена.")

def search_records():
    category = input("Введите категорию для поиска (Доход/Расход): ")

    found_records = [record for record in data if record['category'] == category]

    if found_records:
        print("Найденные записи:")
        for record in found_records:
            print(f"Дата: {record['date']}, Сумма: {record['amount']} руб., Описание: {record['description']}")
    else:
        print("Записи по указанной категории не найдены.")

# Основной код
while True:
    print("\nЛичный финансовый кошелек")
    print("1. Вывод баланса")
    print("2. Добавление записи")
    print("3. Редактирование записи")
    print("4. Поиск по записям")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        add_record()
    elif choice == "3":
        edit_record()
    elif choice == "4":
        search_records()
    elif choice == "5":
        break
    else:
        print("Некорректный выбор.")

print("Спасибо за использование нашего приложения!")