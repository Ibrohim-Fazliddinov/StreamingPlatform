from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from common.choices import PublishStateChoices
from common.mixin import InfoMixin
from content.models.model_category import Category
from django.utils.translation import gettext_lazy as _
from content.models.model_content import VideoContent
from users.models.profile import Profile

User = get_user_model()

def playlist_preview_upload_path(instance, filename):
    """
    Формирует путь загрузки для превью плейлиста.
    Пример: playlist/MOV/2025/03/09/preview.jpg
    """
    return f'playlist/{instance.type}/{timezone.now().strftime("%Y/%m/%d")}/{filename}'



class PlaylistQuerySet(models.QuerySet):
    def published(self):
        """Возвращает только опубликованные плейлисты"""
        return self.filter(state=PublishStateChoices.PUBLISHED)

    def visible_for_user(self, user):
        """Фильтрует плейлисты, которые может видеть пользователь"""
        if user.is_authenticated:
            return self.filter(
                models.Q(state=PublishStateChoices.PUBLISHED) |
                models.Q(owner=user) |
                models.Q(subscription_required=True, owner__subscription=True)
            ).distinct()

        return self.published()

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)

    def visible_for_user(self, user):
        return self.get_queryset().visible_for_user(user)

class Playlist(InfoMixin):
    class PlaylistTypeChoices(models.TextChoices):
        MOVIE = "MOV", _("Movie")
        TV_SHOW = "TVS", _("TV Show")
        SEASON = "SEA", _("Season")
        PLAYLIST = "PLY", _("Playlist")
        WATCH_LATER = "WTL", _("Watch Later")
        LIKED = "LKD", _("Liked")
        WATCH_HISTORY = "WHS", _("History")
        UPLOAD_VIDEOS = "UPD", _("Users upload videos")

    owner = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.CASCADE,
        related_name='playlist_owner',
        default=1
    )
    title = models.CharField(max_length=255)
    type = models.CharField(
        max_length=3,
        choices=PlaylistTypeChoices,
        default="PLY"
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    # tags = models.ForeignKey()
    preview = models.ImageField(
        upload_to=playlist_preview_upload_path,
        default='',
    )
    slug = models.SlugField(
        blank=True,
        null=True
    )
    video = models.ManyToManyField(
        to=VideoContent,
        related_name="ply_video",
        blank=True,
    )
    state = models.CharField(
        max_length=3,
        choices=PublishStateChoices,
        default="PRI"
    )
    category = models.ForeignKey(
        to=Category,
        related_name='playlist',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    subscription_required = models.BooleanField(default=False)

    objects = PlaylistManager()

    def __str__(self):
        return f"{self.type}|{self.title}"

    @property
    def is_season(self):
        return self.type == self.PlaylistTypeChoices.SEASON

    @property
    def is_movie(self):
        return self.type == self.PlaylistTypeChoices.MOVIE

    @property
    def is_show(self):
        return self.type == self.PlaylistTypeChoices.TV_SHOW

    def get_preview_url(self):
        if self.preview:
            return self.preview.url
        return None


class PlaylistVideo(InfoMixin):
    playlist = models.ForeignKey('playlist.Playlist', on_delete=models.CASCADE, related_name="playlist_videos")
    video = models.ForeignKey('content.VideoContent', on_delete=models.CASCADE, related_name="video_playlists")
    order = models.PositiveIntegerField(default=0)  # Порядок видео

    class Meta:
        ordering = ['order', 'updated_at', 'created_at']
        unique_together = ('playlist', 'video')


