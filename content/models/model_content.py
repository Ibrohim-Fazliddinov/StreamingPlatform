from datetime import timedelta
from django.db import models
from comments.models import Comment, Reaction
from common.mixin import InfoMixin
from common.utils import get_video_duration
from content.manager import PersonManager
from content.models.model_category import Category
from content.services import slug_generation

# class VideoQuerySet(models.QuerySet):
#     def published(self):
#         now = timezone.now()
#         return self.filter(
#             state=PublishStateChoices.PUBLISHED,
#             publish_timestamp__lte=now
#         )


class VideoContent(InfoMixin):
    title = models.CharField(verbose_name="Название видеоматериала",
                             max_length=200,
                             db_index=True)

    content = models.FileField(verbose_name="Видео контент",
                               upload_to='content/$Y/%m/%d/')
    preview_image = models.ImageField(verbose_name='Превью',
                                      upload_to='preview/$Y/%m/%d/',
                                      blank=True, null=True,
                                      default=None)
    duration = models.DurationField(verbose_name="Длительность",
                                    blank=True, null=True)

    description = models.TextField(verbose_name="Описание",
                                   default=None,
                                   null=True,
                                   blank=True)

    slug = models.SlugField(verbose_name="Уникальный индикатор",
                            max_length=150,
                            unique=True,
                            db_index=True,
                            blank=False,
                            null=False)

    is_private = models.BooleanField(verbose_name="Сделать видео приватным",
                                     choices=[(True, 'Да'), (False, 'Нет')],
                                     default=False)

    categories_content = models.ManyToManyField(Category,
                                                related_name='categories_content',
                                                blank=True)

    objects = PersonManager()

    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контент"

    def __str__(self):
        return f'{self.title}'

    def get_preview_url(self):
        if self.preview_image:
            return self.preview_image.url
        return None # надо написать автоматическое добавление превью

    def likes_count(self):
        return self.reactions.filter(reaction_type=Reaction.ReactionChoices.LIKE).count()

    def dislikes_count(self):
        return self.reactions.filter(reaction_type=Reaction.ReactionChoices.DISLIKE).count()

    def save(self, *args, **kwargs):
        """ Автоматическое создание slug и длительности видео """
        if not self.slug:
            self.slug = slug_generation(size_slug=150)

        # Автоматическое определение длительности видео
        if self.content and not self.duration:
            try:
                duration = get_video_duration(self.content.path)
                if duration:
                    self.duration = timedelta(seconds=duration)
            except Exception as e:
                print(f"Ошибка при получении длительности видео: {e}")

        super().save(*args, **kwargs)
