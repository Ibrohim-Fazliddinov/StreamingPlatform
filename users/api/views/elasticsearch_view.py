from drf_spectacular.utils import extend_schema_view, extend_schema
from elasticsearch_dsl import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.elasticsearch.document import ContentDocument
from api.elasticsearch.serializer import ContentDocumentSerializer
from content.paginators import ContentPaginator
from content.services import user_status_subscription


@extend_schema_view(
    list=extend_schema(
        summary='Получить список контента',
        description='Получить список контента из Elasticsearch',
        tags=['Контент']
    ),
)
class ElasticsearchView(ListAPIView):
    """
    Представление для поиска и фильтрации контента в Elasticsearch.

    Это представление позволяет:
    - Получить список контента с поддержкой пагинации.
    - Выполнять фильтрацию по категориям.
    - Искать контент по ключевым словам с использованием полнотекстового поиска.
    """

    pagination_class = ContentPaginator
    serializer_class = ContentDocumentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Формирует базовый запрос для получения контента из Elasticsearch.

        Включает фильтрацию по полю `is_private` на основе статуса подписки пользователя.
        """
        queryset = ContentDocument.search().filter(
            "term", is_private=user_status_subscription(self.request.user)
        )
        return queryset

    def search(self, queryset):
        """
        Применяет фильтрацию и поиск по запросу.

        Фильтры:
        - По категориям (`categories_content`): принимает список категорий через запятую.
        - Поисковый запрос (`search`): ищет по полям `title` и `description` с поддержкой fuzzy поиска.
        """
        # Получаем параметры фильтрации из запроса
        categories = self.request.query_params.get('categories_content', None)
        search_term = self.request.query_params.get('search', None)

        # Применяем фильтрацию по категориям
        if categories:
            categories = [cat.strip() for cat in categories.split(',') if cat.strip()]
            if categories:
                # Используем фильтрацию через nested
                queryset = queryset.filter(
                    'nested',
                    path='categories_content',  # Указываем путь к вложенному полю
                    query={
                        'terms': {
                            'categories_content.name': categories  # Ищем по имени категории
                        }
                    }
                )

        # Применяем фильтрацию по поисковому запросу
        if search_term:
            # Создаем запрос с точным совпадением и fuzziness
            query = Q(
                "bool",
                should=[
                    # Точное совпадение с высоким приоритетом
                    Q("match_phrase", title={"query": search_term, "boost": 2.0}),
                    Q("match_phrase", description={"query": search_term, "boost": 1.5}),
                    # Фаззи-поиск с меньшим приоритетом
                    Q("multi_match", query=search_term, fields=["title^1", "description^0.5"], fuzziness="AUTO")
                ],
                minimum_should_match=1  # Требуем хотя бы одно совпадение
            )
            queryset = queryset.query(query)

        return queryset

    def list(self, request, *args, **kwargs):
        """
        Обрабатывает запрос на получение списка контента.

        - Выполняет поиск и фильтрацию с помощью метода `search`.
        - Формирует ответ с пагинацией или без нее.
        """
        # Применяем поиск и фильтрацию
        queryset = self.search(self.get_queryset())

        # Проверяем, требуется ли пагинация
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # Если пагинация не требуется, возвращаем полный список
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)