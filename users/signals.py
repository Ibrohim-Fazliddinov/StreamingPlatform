from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from playlist.models import Playlist
from users.models.profile import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def post_save_user(sender, instance: User, created, **kwargs)-> None:
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_default_playlists(sender, instance, created, **kwargs):
    if created:
        Playlist.objects.create(owner=instance, title="Смотреть позже", type=Playlist.PlaylistTypeChoices.WATCH_LATER)
        Playlist.objects.create(owner=instance, title="Понравившиеся", type=Playlist.PlaylistTypeChoices.LIKED)
        Playlist.objects.create(owner=instance, title="История", type=Playlist.PlaylistTypeChoices.WATCH_HISTORY)