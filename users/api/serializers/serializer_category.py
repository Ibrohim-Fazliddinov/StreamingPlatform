from rest_framework import serializers
from content.api.serializers.serializer_content import ContentSerializer
from content.models.model_category import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели `Category`. Используется для представления категорий с их содержимым.

    Этот сериализатор преобразует объект категории в формат JSON и наоборот.
    Он включает в себя связанные с категорией элементы из модели `Content`,
    которые представлены через поле `categories_content` в модели категории.

    Атрибуты:
        contents (ContentSerializer): Сериализует список объектов `Content`, связанных с категорией.

    Поля:
        - id (int): Уникальный идентификатор категории.
        - name (str): Название категории.
        - contents (list): Список содержимого, связанного с категорией.
    """
    contents = ContentSerializer(many=True, read_only=True, source='categories_content')

    class Meta:
        model = Category
        fields = ['id', 'name', 'contents']
