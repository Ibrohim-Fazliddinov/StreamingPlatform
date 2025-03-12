from ckeditor.fields import RichTextField
from django.db import models
from common.mixin import InfoMixin


class Channel(InfoMixin):
    user = models.ForeignKey(
        to='users.CustomUser',
        on_delete=models.CASCADE,
    )
    title = models.CharField(unique=True, max_length=255)
    description = RichTextField(max_length=400)
    videos = models.PositiveSmallIntegerField(default=0)
    comments = models.PositiveSmallIntegerField(default=0)
    views = models.IntegerField(default=0)
    channel_photo = models.ImageField(upload_to="channel_photos/", blank=True, null=True)
    followers = models.ManyToManyField(
        to='self',
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
