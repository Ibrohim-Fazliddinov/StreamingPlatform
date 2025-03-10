from datetime import datetime
from typing import Any

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

import pytest

from content.models.model_content import Content
from playlist.models import Playlist


class TestPlaylist:

    @pytest.fixture
    def create_fake_video(self) -> ContentFile:
        """ Создаем фикстуру ,которая будет создовать фейковый файл для поля content
            модели Content"""
        video_content = b'Video content'

        # Создаем ContentFile с заданным именем
        video_file = ContentFile(video_content, name='video.mp4')

        # Возвращаем объект ContentFile
        return video_file

    @pytest.fixture
    def create_models(self, create_fake_video, db: Any) -> None:
        """ Создаем экземпляры модели Category, Content, get_user_model"""
        user_object = get_user_model().objects.create_user(username='test_user',
                                                           email='test@example.com',
                                                           password='test_passwor123')

        content_object = Content.objects.create(title='Film',
                                                content=create_fake_video,
                                                description='description_film',
                                                pub_date_time=datetime.now(),
                                                author_content=user_object)

        custom_playlists = Playlist.objects.create(name='test_name',
                                                   author_playlist=user_object)
        custom_playlists.content.add(content_object)

        return custom_playlists

    def test_create_playlists(self, create_models: Content) -> None:
        """Проверяем что запись создана"""
        assert Playlist.objects.count() == 1
