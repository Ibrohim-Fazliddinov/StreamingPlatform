from django.db import models


class Category(models.Model):
    """
             Модель представляющая статистике контента пользователей приложения.

             Атрибуты:
                 id (int): Уникальный идентификатор пользователя добовляется DJANGO автоматически
                 name (str): Название категории
             """
    name = models.CharField(verbose_name="Название категории", max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Кaтегория"
        verbose_name_plural = "Категории"
