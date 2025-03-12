from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


User = get_user_model()

# Проверка, зарегистрирована ли модель User
if admin.site.is_registered(User):
    admin.site.unregister(User)

# @admin.display(description='Фото пользователя', ordering='user__created_at')
#     def profile_photo(self, profile: Profile) -> str:
#         """
#         Метод для отображения фото профиля в админке.
#
#         Аргументы:
#             profile (Profile): Экземпляр модели Profile, для которого нужно отобразить фото.
#
#         Возвращает:
#             str: HTML-код для отображения изображения фото профиля.
#         """
#         return format_html("<img src='{}' width=50>", profile.user_photo.url if profile.user_photo else '')

admin.site.register(User)