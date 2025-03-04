from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from content.api.serializers.serializer_content import ContentSerializer
from content.models.model_content import Content
from content.permissions import ContentViewSetPermissions
from content.services import user_status_subscription


@extend_schema_view(
    retrieve=extend_schema(  # Используем retrieve для GET-запроса на получение одного контента
        summary='Получение контента',
        description='Возвращает данные контента по указанному `slug`.',
        tags=['Контент']
    ),
    create=extend_schema(  # Создание контента, используется POST
        summary='Создание нового контента',
        description='Позволяет создать новый контент.',
        tags=['Контент']
    ),
    update=extend_schema(  # Обновление контента, используется PUT
        summary='Обновление контента',
        description='Обновляет существующий контент.',
        tags=['Контент']
    ),
    destroy=extend_schema(  # Удаление контента, используется DELETE
        summary='Удаление контента',
        description='Удаляет существующий контент.',
        tags=['Контент']
    ),
)
class ContentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    """
    Представление API для работы с моделью `Content`. Реализует стандартные методы:
    - `create` — создание нового контента;
    - `update` — обновление существующего контента;
    - `destroy` — удаление контента;
    - `retrieve` — получение данных конкретного контента по полю `slug`.

    Этот `ViewSet` предоставляет функциональность для создания, обновления,
    удаления и получения экземпляров контента.
    Доступ к контенту ограничен на основе статуса подписки пользователя.
    Только пользователи с действующей подпиской могут
    получить доступ ко всем данным.

    Атрибуты:
        serializer_class (ContentSerializer): Сериализатор для модели `Content`。
        lookup_field (str): Поле, по которому будет осуществляться поиск контента (в данном случае — `slug`).
    """

    serializer_class = ContentSerializer
    lookup_field = 'slug'
    permission_classes = [ContentViewSetPermissions]

    def get_queryset(self):
        """
        Метод для получения списка объектов `Content`.
        Фильтрует доступный контент в зависимости от статуса подписки
        пользователя. Если пользователь имеет активную подписку, возвращаются все записи,
        если нет — только бесплатный контент.

        Возвращает:
            QuerySet: Список объектов `Content`, соответствующий запросу пользователя.
        """
        # Получаем статус подписки пользователя
        status_subscription = user_status_subscription(self.request.user)

        # Если у пользователя есть активная подписка, возвращаем все контенты
        if status_subscription:
            return Content.objects.all()

        # Если у пользователя нет активной подписки, возвращаем только бесплатный контент
        return Content.objects.free()
