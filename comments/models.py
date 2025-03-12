from django.contrib.auth import get_user_model
from django.db import models
from common.mixin import InfoMixin
from content.models.model_content import VideoContent
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Reaction(InfoMixin):
    """
    Модель реакции на видео контент.
    Реакции могут быть двух типов: Лайк и Дизлайк.
    Пользователь может поставить одну реакцию на одно видео.

    Атрибуты:
        user (ForeignKey): Пользователь, который поставил реакцию.
        video (ForeignKey): Видео, к которому относится реакция.
        reaction_type (CharField): Тип реакции (Лайк или Дизлайк).
    Методы:
        __str__: Возвращает строковое представление реакции в формате "Пользователь | Тип реакции | Видео".
    """

    class ReactionChoices(models.TextChoices):
        LIKE = 'LKE', _('Like')
        DISLIKE = 'DIS', _('DisLike')

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='reactions',
        verbose_name='Пользователь'
    )

    video = models.ForeignKey(
        to=VideoContent,
        on_delete=models.CASCADE,
        related_name='reactions',
        verbose_name='Видео'
    )
    reaction_type = models.CharField(
        choices=ReactionChoices.choices,
        max_length=3,
        verbose_name='Тип реакции'
    )

    class Meta:
        unique_together = ('video', 'user')  # Один пользователь - одна реакция на одно видео

    def __str__(self):
        return f'{self.user.username} {self.get_reaction_type_display()} на {self.video.title}'


class Comment(InfoMixin):
    """
    Модель комментария к видео контенту.
    Поддерживает создание вложенных комментариев (ответов).

    Атрибуты:
        comment (TextField): Текст комментария.
        video (ForeignKey): Видео, к которому относится комментарий.
        user (ForeignKey): Пользователь, оставивший комментарий.
        parent (ForeignKey): Родительский комментарий (если это ответ).
        sub_comments (RelatedManager): Связанные под комментарии.
    Методы:
        __str__: Возвращает строковое представление комментария в формате "Комментарий от Пользователь к Видео".
        get_all_replies: Рекурсивно получает все ответы на комментарий и подкомментарии.
    """

    comment = models.TextField(verbose_name="Комментарий")
    video = models.ForeignKey(
        to=VideoContent,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Видео'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пользователь'
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sub_comments',
        verbose_name='Родительский комментарий'
    )

    def __str__(self):
        return f'Комментарий от {self.user.username} к {self.video.title}'

    def get_all_replies(self):
        """
        Рекурсивно получает все под комментарии на текущий комментарий.

        Возвращает:
            QuerySet: Все под комментарии, включая вложенные ответы.
        """
        replies = self.sub_comments.all()
        for reply in replies:
            replies |= reply.get_all_replies()
        return replies
