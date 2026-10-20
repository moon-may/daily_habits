import os
import sqlite3
from functools import wraps

# Пути к файлам
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'daily_habits.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

# Декоратор - подключение к БД
def db_connect(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        con = sqlite3.connect(DB_PATH)
        cursor = con.cursor()
        result = func(cursor, *args, **kwargs)
        con.commit()
        con.close()
        return result
    return wrapper

# Создание файла базы данных
con = sqlite3.connect(DB_PATH)
cursor = con.cursor()

# Чтение скрипта для создания таблиц
with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Выполнение скрипта
cursor.executescript(sql_script)

con.commit()
con.close()