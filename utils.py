import logging

def format_movie_info(title: str, release_year: int, director: str) -> str:
    """Форматирование информации о фильме для вывода пользователю

    Args:
        title (str): Название фильма
        release_year (int): Год выпуска фильма
        director (str): Режиссер фильма

    Returns:
        str: Отформатированная информация о фильме
    """
    return f"Название: {title}\nГод выпуска: {release_year}\nРежиссер: {director}"

def log_error_message(error_message: str):
    """Логирование сообщения об ошибке

    Args:
        error_message (str): Сообщение об ошибке
    """
    logging.error(error_message)

def register_message(message: str):
    """Регистрация сообщения

    Args:
        message (str): Сообщение для регистрации
    """
    logging.info(f"Received message: {message}")
