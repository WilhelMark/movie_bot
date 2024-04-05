import sqlite3
from typing import List, Tuple

# Инициализация соединения с базой данных
def init_db_connection():
    """Инициализация соединения с базой данных"""
    conn = sqlite3.connect("movies.db")
    conn.row_factory = sqlite3.Row
    return conn

# Создание таблицы с фильмами
def create_movies_table(conn):
    """Создание таблицы с фильмами"""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            release_year INTEGER NOT NULL,
            director TEXT NOT NULL
        );
    """)
    conn.commit()

# Добавление фильма в базу данных
def add_movie(conn, title: str, release_year: int, director: str):
    """Добавление фильма в базу данных"""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO movies (title, release_year, director)
        VALUES (?, ?, ?);
    """, (title, release_year, director))
    conn.commit()

# Получение фильма по ID
def get_movie_by_id(conn, movie_id: int) -> Tuple:
    """Получение фильма по ID"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM movies
        WHERE id = ?;
    """, (movie_id,))
    return cursor.fetchone()

# Получение всех фильмов из базы данных
def get_all_movies(conn) -> List:
    """Получение всех фильмов из базы данных"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM movies;
    """)
    return cursor.fetchall()

# Удаление фильма из базы данных
def delete_movie(conn, movie_id: int):
    """Удаление фильма из базы данных"""
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM movies
        WHERE id = ?;
    """, (movie_id,))
    conn.commit()

# Закрытие соединения с базой данных
def close_db_connection(conn):
    """Закрытие соединения с базой данных"""
    conn.close()
