import sqlite3

# Создание файла базы данных
con = sqlite3.connect('daily_habits.db')
cursor = con.cursor()

# Чтение скрипта для создания таблиц
with open('schema.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Выполнение скрипта
cursor.executescript(sql_script)

con.commit()
con.close()