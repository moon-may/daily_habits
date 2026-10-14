from database import db_connect


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

@db_connect
def get_habits(cursor):
    '''Получить все привычки в БД'''
    cursor.execute('''SELECT * FROM habits''')
    return cursor.fetchall()


@db_connect
def get_completions(cursor, habit_id, start_date, end_date):
    '''Получить данные по привычкам за период'''
    cursor.execute('''SELECT today_value FROM completed 
                    WHERE habit_id=? AND today_date BETWEEN ? AND ?''',
                    (habit_id, start_date, end_date))
