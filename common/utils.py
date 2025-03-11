from __future__ import annotations
from typing import TYPE_CHECKING, Union, List
import ffmpeg

if TYPE_CHECKING:
    from django.urls.resolvers import URLPattern


def filter_routes(urls: List[Union[URLPattern, str]], allowed_patterns: tuple[str, ...]) -> List[Union[URLPattern, str]]:
    """
    Фильтрация маршрутов: оставляет только URL-адреса, содержащие шаблоны из списка разрешенных.

    :param urls: Список URL-адресов для фильтрации.
    :param allowed_patterns: Кортеж шаблонов для разрешения.
    :return: Отфильтрованный список URL-адресов.
    """
    filtered_urls = []
    for url in urls:
        route = str(url.pattern)  # Получаем строковое представление маршрута
        if any(pattern in route for pattern in allowed_patterns):
            filtered_urls.append(url)
    return filtered_urls


def get_video_duration(file_path):
    try:
        probe = ffmpeg.probe(file_path)
        duration = float(probe['format']['duration'])
        return duration
    except Exception as e:
        print(f"Ошибка при определении продолжительности видео: {e}")
        return None
