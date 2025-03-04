from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from users.models.profile import Profile

User = get_user_model()

# Проверка, зарегистрирована ли модель User
if admin.site.is_registered(User):
    admin.site.unregister(User)


class ProfileAdmin(admin.TabularInline):
    """
    Встраиваемый интерфейс администрирования для модели Profile,
    который добавляет вкладку с профилем пользователя на страницу редактирования пользователя.

    Атрибуты:
        * `model` (Profile): Модель, которая будет отображаться в виде встроенной формы.
        * `list_display` (list[str]): Список полей, отображаемых в виде таблицы на странице редактирования.
        * `list_display_links` (list[str]): Поля, которые будут ссылками на объект в таблице.
    """
    model = Profile
    list_display = ["user", "profile_photo", "description"]  # Поля, которые будут отображаться в списке объектов
    list_display_links = ["user", "description"]  # Поля, которые будут ссылками на объект

    # def brief_info(self, profile: Profile) -> str:
    #     """
    #     Метод для отображения краткой информации о пользователе в админке.

    #     Аргументы:
    #         profile (Profile): Экземпляр модели Profile, для которого нужно получить информацию.

    #     Возвращает:
    #         str: Строка, содержащая полное имя пользователя и количество символов в его биографии.
    #     """
    #     return f"{profile.user.first_name} {profile.user.last_name} написал(а) {len(profile.bio)} символов"

    @admin.display(description='Фото пользователя', ordering='user__created_at')
    def profile_photo(self, profile: Profile) -> str:
        """
        Метод для отображения фото профиля в админке.

        Аргументы:
            profile (Profile): Экземпляр модели Profile, для которого нужно отобразить фото.

        Возвращает:
            str: HTML-код для отображения изображения фото профиля.
        """
        return format_html("<img src='{}' width=50>", profile.user_photo.url if profile.user_photo else '')

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Кастомный интерфейс администрирования для модели User, который позволяет управлять пользователями
    и их профилями в админке Django.

    Атрибуты:
        * `fieldsets` (tuple[tuple[str, dict]]): Определяет группы полей и их описание на странице редактирования пользователя.
        * `add_fieldsets` (tuple[tuple[str, dict]]): Определяет поля для создания нового пользователя.
        * `list_display` (tuple[str]): Поля, отображаемые в списке пользователей в админке.
        * `list_display_links` (tuple[str]): Поля, которые будут ссылками для перехода к странице редактирования.
        * `list_filter` (tuple[str]): Фильтры, доступные для быстрого поиска пользователей.
        * `search_fields` (tuple[str]): Поля, по которым можно осуществлять поиск пользователей.
        * `ordering` (tuple[str]): Порядок сортировки пользователей в списке.
        * `filter_horizontal` (tuple[str]): Горизонтальные фильтры для групп и разрешений.
        * `readonly_fields` (tuple[str]): Поля, которые только для чтения и не могут быть изменены.
        * `inlines` (tuple[admin.TabularInline]): Включает встроенные формы, такие как ProfileAdmin.
    """

    fieldsets = (
        (
            None,
            {
                "fields": ("username", "email"),
                "description": "Основные поля пользователя, такие как имя пользователя и контактная информация."
            }
        ),
        (_('Личная информация'),
         {
             "fields": ("first_name", "last_name", 'country'),
             "description": "Информация о личных данных пользователя."
        }),
        (_('Информация о действиях'),
         {
             "fields": ("last_login",),
             "description": "Информация о последнем входе и дате создания пользователя."
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),)

    list_display = ("id", "get_full_name", "email",)
    """
    Поля, отображаемые в списке пользователей в админке.
    """

    list_display_links = ("id", "get_full_name",)
    """
    Поля в списке пользователей, которые являются ссылками для перехода к странице редактирования.
    """

    search_fields = ("first_name", "last_name", "email",)
    """
    Поля, по которым можно искать пользователей в админке.
    """

    ordering = ("-id", "last_login",)
    """
    Порядок сортировки пользователей в списке админки.
    """

    readonly_fields = ("last_login",)
    """
    Поля 'last_login' и 'created_at', которые только для чтения и не могут быть изменены.
    """

    inlines = (ProfileAdmin,)
    """
    Включает встроенный интерфейс для управления профилями пользователей.
    """
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active')
