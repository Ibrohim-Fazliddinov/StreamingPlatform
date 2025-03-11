from django.contrib.auth import get_user_model
from django.db import models

from common.mixin import InfoMixin
from content.models.model_content import VideoContent
from django.utils.translation import gettext_lazy as _


# from content.models.model_content import Content


# class Comment(models.Model):
#     """
#            Модель представляющая  комментарии к контенту пользователей приложения.
#
#            Атрибуты:
#                id (int): Уникальный идентификатор пользователя добовляется DJANGO автоматически
#                comment (str): Текст комментария
#                content (Content): Ссылка на контент, внешний ключ модели Content
#                pub_date_time (datetime): Дата публикации комментария
#                author_comment (get_user_model): Автор комментария, , внешний ключ модели get_user_model
#            """
#     comment = models.TextField(verbose_name='Коментарий')
#     content = models.ForeignKey(Content, related_name='comments', on_delete=models.CASCADE)
#     pub_date_time = models.DateTimeField(verbose_name="Дата и время публикации комментария", auto_now_add=True)
#     author_comment = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author_comment')
#
#     def __str__(self):
#         return f'{self.comment}'
#
#     class Meta:
#         verbose_name = "Коментарий"
#         verbose_name_plural = "Коментарии"
User = get_user_model()

class Reaction(InfoMixin):
    class ReactionChoices(models.TextChoices):
        LIKE = 'LKE', _('Like')
        DISLIKE = 'DIS', _('DisLike')

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='reactions'
    )

    video = models.ForeignKey(
        to=VideoContent,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    reaction_type = models.CharField(
        choices=ReactionChoices.choices,
        max_length=3,
    )

    class Meta:
        unique_together = ('video', 'user')  # Один пользователь - одна реакция на одно видео

    def __str__(self):
        return f'{self.user.username} {self.get_reaction_type_display()} на {self.video.title}'



class Comment(InfoMixin):
    comment = models.TextField(verbose_name="Комментарий")
    video = models.ForeignKey(
        to=VideoContent,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sub_comments'
    )

    def __str__(self):
        return f'Комментарий от {self.user.username} к {self.video.title}'

    def get_all_replies(self):
        """ Получение всех подкомментариев рекурсивно """
        replies = self.sub_comments.all()
        for reply in replies:
            replies |= reply.get_all_replies()
        return replies