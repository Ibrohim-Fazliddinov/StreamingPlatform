from rest_framework.pagination import PageNumberPagination


class ContentPaginator(PageNumberPagination):
    page_size = 50  # Количество элементов на одной странице
    max_page_size = 100  # Максимальный размер страницы
    page_query_param = 'page'  # Параметр для страницы
    page_size_query_param = 'page_size'  # Параметр для размера страницы
