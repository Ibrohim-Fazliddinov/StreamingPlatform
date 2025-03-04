from rest_framework import serializers
from content.models.model_content import Content


class ContentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели `Content`. Преобразует объекты контента в формат JSON и наоборот.

    Этот сериализатор используется для представления отдельных элементов контента, таких как статьи, посты и т.п.
    Он включает в себя информацию о контенте, связанную с полями модели `Content`, такими как заголовок, описание,
    изображение, категория и автор.

    Атрибуты:
        - id (int): Уникальный идентификатор контента.
        - title (str): Заголовок контента.
        - content (str): Основной текст контента.
        - description (str): Описание контента.
        - preview_image (str): Изображение-превью контента.
        - slug (str): Слаг (человекочитаемая часть URL) для контента.
        - pub_date_time (datetime): Дата и время публикации контента.
        - categories_content (list): Список категорий, связанных с контентом.
        - is_private (bool): Статус приватности контента (доступен только определенным пользователям).
        - author_content (str): Автор контента.
    """
    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'content',
            'description',
            'preview_image',
            'slug',
            'pub_date_time',
            'categories_content',
            'is_private',
            'author_content'
        ]
