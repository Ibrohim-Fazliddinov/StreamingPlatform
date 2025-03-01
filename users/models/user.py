from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
)

from users.managers.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    """
    Кастомная модель пользователя, которая расширяет базовые классы AbstractBaseUser и PermissionsMixin Django.

    Данная модель представляет пользователя в системе и содержит несколько ключевых полей для хранения
    информации о пользователе, таких как юзернейм, email и номер телефона. Также включает поля для
    отслеживания времени последнего входа, даты создания и даты изменения учетной записи.

    Атрибуты:
        username (CharField): Уникальный юзернейм пользователя.
        first_name (CharField): Имя пользователя. Необязательное поле.
        second_name (CharField): Фамилия пользователя. Необязательное поле.
        email (EmailField): Уникальный email пользователя.
        phone_number (PhoneNumberField): Уникальный номер телефона пользователя. Необязательное поле.
        created_at (DateTimeField): Дата создания учетной записи. Устанавливается по умолчанию на текущее время.
        last_login (DateTimeField): Дата и время последнего входа пользователя. Устанавливается автоматически при входе.

    Методы:
            objects (UserManager): Пользовательский менеджер для управления учетными записями.
    """

    class Role(models.TextChoices):
        CUSTOMER = 'CUS', _('Клиент')
        ADMIN = 'ADM', _('Администратор')
        MODERATOR = 'MOD', _('Модератор')
        CONTENT_MAKER = 'CNM', _('КонетнтМейкер')
        DEVELOPER = 'DEV', _('Разработчик')

    username = models.CharField(
        unique=True,
        max_length=285,
        verbose_name="Ваш юзернейм"
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Фамилия"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Ваш email"
    )
    phone_number = PhoneNumberField(
        unique=True,
        verbose_name="Номер телефона",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )

    last_login = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего входа",
        null=True
    )

    user_role = models.CharField(
        max_length=3,
        choices=Role.choices,
        default=Role.CUSTOMER,
        verbose_name='Роль | Пользователя'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Статус персонала"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активен"
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        app_label = 'users'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def get_full_name(self):
        return f"{self.first_name}|{self.last_name}"

    def __str__(self):

        telephone = self.phone_number
        role = self.get_user_role_display()  # Получаем текстовое представление роли
        return f'{self.get_full_name} | {self.pk} | {role} | {telephone}'
