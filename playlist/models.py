from ckeditor.fields import RichTextField
from common.choices import PublishStateChoices
from common.mixin import InfoMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


def playlist_preview_upload_path(instance, filename):
    """
    Генерирует путь для загрузки превью плейлиста.
    Формат пути: playlist/<тип>/<год>/<месяц>/<день>/<имя файла>

    Аргументы:
        instance (Playlist): Экземпляр плейлиста.
        filename (str): Оригинальное имя файла.

    Возвращает:
        str: Сгенерированный путь к файлу превью.
    """
    return f'playlist/{instance.type}/{timezone.now().strftime("%Y/%m/%d")}/{filename}'


class PlaylistQuerySet(models.QuerySet):
    """
    Кастомный QuerySet для фильтрации и получения плейлистов на основе их статуса и прав пользователя.
    Предоставляет методы для получения опубликованных и доступных пользователю плейлистов.
    """

    def published(self):
        """
        Возвращает только опубликованные плейлисты.

        Возвращает:
            QuerySet: QuerySet с опубликованными плейлистами.
        """
        return self.filter(state=PublishStateChoices.PUBLISHED)

    def visible_for_user(self, user):
        """
        Возвращает плейлисты, доступные конкретному пользователю.
        Авторизованные пользователи могут видеть свои собственные, опубликованные или требующие подписки плейлисты (если у них есть подписка).

        Аргументы:
            user (User): Пользователь, чьи права доступа проверяются.

        Возвращает:
            QuerySet: QuerySet с плейлистами, доступными пользователю.
        """
        if user.is_authenticated:
            return self.filter(
                models.Q(state=PublishStateChoices.PUBLISHED) |
                models.Q(owner=user) |
                models.Q(subscription_required=True, owner__subscription=True)
            ).distinct()

        return self.published()


class PlaylistManager(models.Manager):
    """
    Кастомный менеджер для модели Playlist, использующий PlaylistQuerySet для фильтрации и проверки видимости.
    """

    def get_queryset(self):
        """
        Возвращает базовый QuerySet для менеджера с использованием PlaylistQuerySet.

        Возвращает:
            PlaylistQuerySet: Базовый QuerySet для плейлистов.
        """
        return PlaylistQuerySet(self.model, using=self._db)

    def visible_for_user(self, user):
        """
        Возвращает плейлисты, видимые конкретному пользователю.

        Аргументы:
            user (User): Пользователь, чьи права доступа проверяются.

        Возвращает:
            QuerySet: QuerySet с видимыми плейлистами.
        """
        return self.get_queryset().visible_for_user(user)


class Playlist(InfoMixin):
    """
    Модель плейлиста, представляющая коллекцию видео.
    Плейлист может относиться к разным категориям (например, фильм, сериал) и содержать превью изображение.
    Поддерживает фильтрацию по видимости и статусу.
    """

    class PlaylistTypeChoices(models.TextChoices):
        MOVIE = "MOV", _("Фильм")
        TV_SHOW = "TVS", _("Сериал")
        SEASON = "SEA", _("Сезон")
        PLAYLIST = "PLY", _("Плейлист")
        WATCH_LATER = "WTL", _("Посмотреть позже")
        LIKED = "LKD", _("Понравилось")
        WATCH_HISTORY = "WHS", _("История просмотра")
        UPLOAD_VIDEOS = "UPD", _("Загруженные видео")

    owner = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.CASCADE,
        related_name='playlist_owner',
        default=1,
        verbose_name='Владелец'
    )
    title = models.CharField(max_length=255, verbose_name='Название')
    type = models.CharField(
        max_length=3,
        choices=PlaylistTypeChoices.choices,
        default="PLY",
        verbose_name='Тип плейлиста'
    )
    description = RichTextField(
        blank=True,
        null=True
    )
    preview = models.ImageField(
        upload_to=playlist_preview_upload_path,
        default='',
        verbose_name='Превью'
    )
    slug = models.SlugField(blank=True, null=True, verbose_name='Слаг')
    video = models.ManyToManyField(
        to='content.VideoContent',
        related_name="ply_video",
        blank=True,
        verbose_name='Видео'
    )
    state = models.CharField(
        max_length=3,
        choices=PublishStateChoices,
        default="PRI",
        verbose_name='Статус публикации'
    )
    category = models.ForeignKey(
        to='content.Category',
        related_name='playlist',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    subscription_required = models.BooleanField(default=False, verbose_name='Требуется подписка')

    objects = PlaylistManager()

    def __str__(self):
        return f"{self.type}|{self.title}"

    def get_preview_url(self):
        """
        Возвращает URL изображения превью плейлиста.

        Возвращает:
            str или None: URL превью или None, если не установлено.
        """
        if self.preview:
            return self.preview.url
        return None


class PlaylistVideo(InfoMixin):
    """
    Модель связи видео с плейлистом, позволяющая задать порядок отображения.
    Гарантирует уникальность пары (плейлист, видео).
    """

    playlist = models.ForeignKey(
        'playlist.Playlist',
        on_delete=models.CASCADE,
        related_name="playlist_videos",
        verbose_name='Плейлист'
    )
    video = models.ForeignKey(
        'content.VideoContent',
        on_delete=models.CASCADE,
        related_name="video_playlists",
        verbose_name='Видео'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order', 'updated_at', 'created_at']
        unique_together = ('playlist', 'video')



