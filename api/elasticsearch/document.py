import logging
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from StreamingPlatform import settings
from content.models.model_category import Category
from content.models.model_content import VideoContent

logger = logging.getLogger('duration_request_view')

russian_analyzer = analyzer(
    'russian',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"]
)


@registry.register_document
class ContentDocument(Document):
    """
    Документ для модели Content, который будет индексироваться в Elasticsearch.
    """
    title = fields.TextField(attr='title', fields={'raw': fields.KeywordField()})
    description = fields.TextField(attr='description', analyzer=russian_analyzer)
    preview_image = fields.KeywordField(attr='preview_image_url')
    slug = fields.KeywordField(attr='slug')
    pub_date_time = fields.DateField(attr='pub_date_time')
    is_private = fields.BooleanField(attr='is_private')

    # Связь ManyToMany с категориями, индексируем как вложенные объекты
    categories_content = fields.NestedField(properties={
        'name': fields.TextField(attr='name')
    })

    # Данные об авторе контента
    author_content = fields.ObjectField(properties={
        'username': fields.KeywordField(attr='username'),
        'email': fields.KeywordField(attr='email')
    })

    class Index:
        # Название индекса Elasticsearch
        name = 'content'

    class Django:
        model = VideoContent  # Модель, связанная с этим документом

    @staticmethod
    def get_instances_from_related(related_instance):
        """
        Эта функция нужна для того, чтобы связать категории с контентом.
        Она ищет все экземпляры контента, связанные с конкретной категорией.
        """
        if isinstance(related_instance, Category):
            # Используем обратную связь через Content, чтобы получить все контенты, связанные с категорией.
            return VideoContent.objects.filter(categories_content=related_instance)
        return []

    def prepare_preview_image(self, instance):
        """
        Возвращаем абсолютный URL к изображению превью.
        Формируем полный URL, используя MEDIA_URL.
        """
        if instance.preview_image:
            return settings.MEDIA_URL + instance.preview_image.name
        return None
