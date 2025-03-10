from django.contrib.auth import get_user_model
from django.db import models

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
class Comment:
    pass