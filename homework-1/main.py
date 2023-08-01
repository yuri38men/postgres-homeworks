"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='ogr25men')
cursor = conn.cursor()

# Имя файла и таблицы для заполнения данными
files = {
    "employees": "north_data/employees_data.csv",
    "customers": "north_data/customers_data.csv",
    "orders": "north_data/orders_data.csv"
}

# Заполнение таблиц данными из файлов
for table_name, file_path in files.items():
    with open(file_path, "r") as file:
        csv_data = csv.reader(file, delimiter=",")
        next(csv_data)  # Пропускаем заголовок CSV-файла

        for row in csv_data:
            # Формируем SQL-запрос для вставки данных в таблицу
            sql = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(row))})"
            cursor.execute(sql, row)

# Фиксируем изменения и закрываем соединение
conn.commit()
cursor.close()
conn.close()

print("Данные успешно загружены в таблицы.")
