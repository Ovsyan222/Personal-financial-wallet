1. Импорт необходимых модулей: #эти строки импортируют модуль json (для работы с JSON-данными) и модуль os (для работы с операционной системой).
import json
import os

2. Переменная для хранения данных: #это переменная, в которой указано имя файла для хранения данных о финансах.
data_file = "finances.json"

3. Чтение данных из файла: #этот блок проверяет наличие файла с данными о финансах. Если файл существует, данные загружаются из него в переменную data. В противном случае переменная data инициализируется пустым списком.

if os.path.exists(data_file):
    with open(data_file, "r") as file:
        data = json.load(file)
else:
    data = []

4. Функция save_data() для сохранения данных: #эта функция сохраняет данные в файл finances.json, используя модуль json. Данные сохраняются с отступом в 4 пробела для удобочитаемости.

def save_data():
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

5. Функция show_balance() для вывода текущего баланса: #эта функция вычисляет и выводит текущий баланс, общие доходы и расходы на основе данных в переменной data.

def show_balance():
    total_income = sum(record['amount'] for record in data if record['category'] == 'Доход')
    total_expense = sum(record['amount'] for record in data if record['category'] == 'Расход')
    total_balance = total_income - total_expense

    print(f"Текущий баланс: {total_balance} руб.")
    print(f"Доходы: {total_income} руб.")
    print(f"Расходы: {total_expense} руб.")

6. Функция add_record() для добавления новой записи: #эта функция позволяет пользователю добавить новую запись о финансах, запрашивая у пользователя дату, категорию, сумму и описание.

def add_record():
    record = {}
    record['date'] = input("Введите дату (гггг-мм-дд): ")
    record['category'] = input("Введите категорию (Доход/Расход): ")
    record['amount'] = float(input("Введите сумму: "))
    record['description'] = input("Введите описание: ")

    data.append(record)
    save_data()
    print("Запись успешно добавлена.")

7. Функция edit_record() для редактирования существующей записи: #эта функция позволяет редактировать существующую запись о финансах по заданной пользователем дате.

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

8. Функция search_records() для поиска записей по категории: #эта функция позволяет пользователю искать записи о финансах по указанной категории (Доход или Расход) и выводит результаты поиска.

def search_records():
    category = input("Введите категорию для поиска (Доход/Расход): ")

    found_records = [record for record in data if record['category'] == category]

    if found_records:
        print("Найденные записи:")
        for record in found_records:
            print(record)
    else:
        print("Записи не найдены.")
