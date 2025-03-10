from django.db import models


class PersonQuerySet(models.QuerySet):
    """
    Кастомный QuerySet для модели `Person`, который добавляет методы фильтрации
    для получения платных и бесплатных записей на основе поля `is_private`.

    Методы:
        - paid() - фильтрует записи, где `is_private=True` (платный контент).
        - free() - фильтрует записи, где `is_private=False` (бесплатный контент).
    """

    def paid(self):
        """
        Возвращает записи, у которых `is_private=True`, что означает платный контент.

        Возвращаемое значение:
            QuerySet: Список объектов `Person`, где `is_private=True`.
        """
        return self.filter(is_private=True)

    def free(self):
        """
        Возвращает записи, у которых `is_private=False`, что означает бесплатный контент.

        Возвращаемое значение:
            QuerySet: Список объектов `Person`, где `is_private=False`.
        """
        return self.filter(is_private=False)


class PersonManager(models.Manager):
    """
    Кастомный менеджер для модели `Person`, который использует `PersonQuerySet`.
    Этот менеджер предоставляет удобные методы для получения платных и бесплатных записей.

    Методы:
        - paid() - возвращает платные записи.
        - free() - возвращает бесплатные записи.
    """

    def get_queryset(self):
        """
        Возвращает экземпляр `PersonQuerySet` для выполнения кастомных операций.

        Возвращаемое значение:
            PersonQuerySet: Экземпляр `PersonQuerySet` для модели `Person`.
        """
        return PersonQuerySet(self.model, using=self._db)

    def paid(self):
        """
        Возвращает все платные записи с помощью метода `paid()` из `PersonQuerySet`.

        Возвращаемое значение:
            QuerySet: Список платных записей `Person`, где `is_private=True`.
        """
        return self.get_queryset().paid()

    def free(self):
        """
        Возвращает все бесплатные записи с помощью метода `free()` из `PersonQuerySet`.

        Возвращаемое значение:
            QuerySet: Список бесплатных записей `Person`, где `is_private=False`.
        """
        return self.get_queryset().free()
