from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from accounts.models import User

User = get_user_model()
COUNTRY_CHOICES = [
    ('other', 'Международный'),
    ('AZ', 'Азербайджан'),
    ('AM', 'Армения'),
    ('BY', 'Беларусь'),
    ('KZ', 'Казахстан'),
    ('KG', 'Кыргызстан'),
    ('MD', 'Молдова'),
    ('RU', 'Россия'),
    ('TJ', 'Таджикистан'),
    ('TM', 'Туркменистан'),
    ('UZ', 'Узбекистан'),
    #
]


class Profile(models.Model):
    """
    Модель, представляющая профиль пользователя.

    Атрибуты:
        user (OneToOneField): Однонаправленная связь с моделью User. Обеспечивает наличие 
            у каждого пользователя только одного профиля.
        description (TextField): Поле для описания пользователя или биографии.
        user_photo (ImageField): Поле для фотографии пользователя, изображения загружаются в 
            директорию 'profile_photos/'. Это поле не обязательно для заполнения.
        country (CharField): Поле, содержащее информацию о стране пользователя, с предустановленными 
            вариантами выбора для стран СНГ и других. По умолчанию устанавливается IP-адрес хоста.
    
    Метаданные:
        verbose_name (str): Человеческое имя модели в единственном числе.
        verbose_name_plural (str): Человеческое имя модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление профиля пользователя, основанное на его электронной почте.
    """
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name=_("Пользователь"),
        primary_key=True
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        blank=True
    )
    user_photo = models.ImageField(
        upload_to='profile_photos/',
        verbose_name=_("Фото пользователя"),
        default=None,
        blank=True
    )
    country = models.CharField(
        max_length=5,
        choices=COUNTRY_CHOICES,
        verbose_name=_("Страна"),
    )

 
    class Meta:
        verbose_name = _("Профиль")
        verbose_name_plural = _("Профили")

    def __str__(self):
        return self.user.email

    # def get_absolute_url(self):
    #     """Возвращает абсолютный URL для просмотра профиля."""
    #     return reverse("Профиль_detail", kwargs={"pk": self.pk})
