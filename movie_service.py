from movie_parser import get_movie_info_from_imdb, get_movie_watch_info_from_kinopoisk
from database import init_db_connection, add_movie, get_movie_by_id

def search_movie_info(movie_title: str) -> str:
    """Поиск информации о фильме и сохранение в базу данных

    Args:
        movie_title (str): Название фильма

    Returns:
        str: Результат поиска информации о фильме
    """
    # Получение информации о фильме с IMDb
    imdb_info = get_movie_info_from_imdb(movie_title)
    if imdb_info:
        # Сохранение информации о фильме в базу данных
        conn = init_db_connection()
        add_movie(conn, imdb_info["title"], imdb_info["release_year"], imdb_info["director"])
        conn.close()
        return f"Информация о фильме '{imdb_info['title']}' добавлена в базу данных."
    else:
        return "Информация о фильме не найдена."

def search_movie_watch_info(movie_title: str) -> str:
    """Поиск информации о возможностях просмотра фильма

    Args:
        movie_title (str): Название фильма

    Returns:
        str: Результат поиска информации о возможностях просмотра фильма
    """
    # Получение информации о возможностях просмотра фильма с КиноПоиск
    kinopoisk_info = get_movie_watch_info_from_kinopoisk(movie_title)
    if kinopoisk_info:
        result = f"Кинотеатры: {', '.join(kinopoisk_info['cinema'])}\n"
        result += f"Онлайн: {', '.join(kinopoisk_info['online'])}"
        return result
    else:
        return "Информация о возможностях просмотра фильма не найдена."
