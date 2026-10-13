
import sqlite3
from functools import wraps

# Декоратор - подключение к БД
def db_connect(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        con = sqlite3.connect('daily_habits.db')
        cursor = con.cursor()
        result = func(cursor, *args, **kwargs)
        con.commit()
        con.close()
        return result
    return wrapper

@db_connect
def add_habit(cursor, habit_data):
    '''Добавление новой привычки'''
    cursor.execute('''INSERT INTO habits (habit_name, habit_type, unit, goal) 
                    VALUES (?, ?, ?, ?)''', habit_data)

    
@db_connect
def remove_habit(cursor, habit_id):
    '''Удаление существующей привычки'''
    cursor.execute('''DELETE FROM habits WHERE id=?''', habit_id)


@db_connect
def add_progress(cursor, habit_values):
    '''Добавление текущего выполнения'''
    cursor.execute('''INSERT INTO completed (today_value, habit_id) VALUES (?, ?)''', 
                   habit_values)


@db_connect
def change_progress(cursor, today_daily, habit_id, today_date):
    '''Изменение текущего выполнения'''
    cursor.execute('''UPDATE completed SET today_daily=? WHERE habit_id=? AND today_date=?''',
                   (today_daily, habit_id, today_date))

