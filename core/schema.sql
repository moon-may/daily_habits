CREATE TABLE IF NOT EXISTS habits(
    id INTEGER PRIMARY KEY,
    habit_name TEXT NOT NULL,
    habit_type TEXT NOT NULL,
    unit TEXT,
    goal REAL,
    created_date DATE);

CREATE TABLE IF NOT EXISTS completed(
    id INTEGER PRIMARY KEY,
    today_value REAL,
    today_date DATE,
    habit_id INTEGER,
    FOREIGN KEY (habit_id) REFERENCES habits(id) 
);