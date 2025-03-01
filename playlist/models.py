# import re
# from django.contrib.auth import get_user_model
# from django.db import models
# from django_currentuser.middleware import get_current_user
# from content.models.model_content import Content
#
#
# class Playlist(models.Model):
#     # при удалении плейлиста пользователем записи в промежуточной модели не будут удаляться поэтому
#     # необходимо реализавать удаление связанных обектов вручную
#     """
#        Модель представляющая плейлисты пользователей приложения.
#
#        Атрибуты:
#            id (int): Уникальный идентификатор пользователя добовляется DJANGO автоматически
#            title (str): Название плейлиста
#            content (FileField): id контента модели Content
#            author_content (get_user_model): id Автора плейлиста, , внешний ключ модели get_user_model
#     """
#     name = models.CharField(
#         verbose_name='Название плейлиста',
#         max_length=250,
#         null=True,
#         blank=True,
#         db_default=None
#     )
#     content = models.ManyToManyField(
#         Content,
#         related_name='content_playlist',
#         blank=True
#     )
#     author_playlist = models.ForeignKey(
#         get_user_model(),
#         verbose_name='Автор плейлиста',
#         on_delete=models.CASCADE,
#         related_name='author_playlist'
#     )
#
#     @property
#     def default_name_playlist(self) -> str:
#         """Если пользователь не укажет название плейлиста ,оно будет добавлено автоматически"""
#         # получаем текущего пользователя
#         current_user = get_current_user()
#         # получаем плейлисты текущего пользователя
#         custom_playlists = Playlist.objects.filter(author_playlist=current_user.id)
#
#         names = []
#         # получаем названия плейлистов сгенерированных автоматически текущего пользователя
#         for playlist in custom_playlists:
#             if 'Новый плейлист' in playlist.name:
#                 names.append(playlist.name)
#
#         if not names:
#             # если нет плейлистов соответствующих условию возвращаеи название
#             return 'Новый плейлист1'
#         else:
#             # определяем плейлист с максимальным числовым значением в конце
#             max_name = max(names)
#             match = re.search(r'\d+$', max_name)
#             if match:
#                 number = int(match.group())
#                 # увеличиваем на единицу числовое значение и возвращаем его ка результат
#                 return f"{max_name[:-len(str(number))]}{number + 1}"
#             return max_name
#
#     def save(self, *args, **kwargs):
#         """Переопределяем метод save дляя автоматического добовления названия плейлиста"""
#         if self.name is None:
#             self.name = self.default_name_playlist
#         super().save(*args, **kwargs)
