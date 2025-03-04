from rest_framework.pagination import PageNumberPagination


class ContentPaginator(PageNumberPagination):
    """
    Класс пагинации для контента, использующий нумерацию страниц.

    Настройки:
    - `page_size`: определяет количество элементов на странице.
    - `max_page_size`: максимальное количество элементов на странице.
    - `page_query_param`: параметр запроса для указания страницы.
    - `page_size_query_param`: параметр запроса для указания размера страницы.
    """
    page_size = 50  # Количество элементов на одной странице
    max_page_size = 100  # Максимальный размер страницы
    page_query_param = 'page'  # Параметр для страницы
    page_size_query_param = 'page_size'  # Параметр для размера страницы
