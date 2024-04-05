import requests
from bs4 import BeautifulSoup

def get_movie_info_from_imdb(movie_title: str) -> dict:
    """Получение информации о фильме с сайта IMDb

    Args:
        movie_title (str): Название фильма

    Returns:
        dict: Информация о фильме в виде словаря
    """
    base_url = "https://www.imdb.com/find"
    params = {"q": movie_title, "s": "tt"}
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    movie_container = soup.select_one(".result_text > a")
    if movie_container:
        movie_url = f"https://www.imdb.com{movie_container['href']}"
        movie_response = requests.get(movie_url)
        movie_soup = BeautifulSoup(movie_response.text, "html.parser")
        title = movie_soup.select_one("h1").text.strip()
        release_year = movie_soup.select_one("#titleYear > a").text.strip()
        director = movie_soup.select_one(".credit_summary_item > a").text.strip()
        return {"title": title, "release_year": release_year, "director": director}
    return {}

def get_movie_watch_info_from_kinopoisk(movie_title: str) -> dict:
    """Получение информации о возможностях просмотра фильма с сайта КиноПоиск

    Args:
        movie_title (str): Название фильма

    Returns:
        dict: Информация о возможностях просмотра фильма в виде словаря
    """
    base_url = "https://www.kinopoisk.ru/name/"
    response = requests.get(f"{base_url}{movie_title}/")
    soup = BeautifulSoup(response.text, "html.parser")
    watch_containers = soup.select(".watch-item")
    result = {"cinema": [], "online": []}
    for container in watch_containers:
        title = container.select_one(".title").text.strip()
        if "Кинотеатры" in title:
            cinema_containers = container.select(".cinema-item")
            for cinema_container in cinema_containers:
                cinema_name = cinema_container.select_one(".cinema-name").text.strip()
                result["cinema"].append(cinema_name)
        elif "Интернет" in title:
            online_containers = container.select(".online-item")
            for online_container in online_containers:
                online_name = online_container.select_one(".name").text.strip()
                result["online"].append(online_name)
    return result
