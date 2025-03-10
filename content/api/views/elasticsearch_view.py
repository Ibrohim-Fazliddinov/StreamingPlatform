from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView
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
    pagination_class = ContentPaginator
    serializer_class = ContentDocumentSerializer

    def get_queryset(self):
        """
        Переопределяем метод для фильтрации данных по полю `is_private`
        на основе статуса подписки пользователя.
        """
        queryset = ContentDocument.search().filter("term", is_private=user_status_subscription(self.request.user))
        return queryset

    def search(self, queryset):
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
            queryset = queryset.query('multi_match', query=search_term, fields=['title', 'description'])

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.search(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
