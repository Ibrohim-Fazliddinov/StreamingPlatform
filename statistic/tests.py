from datetime import datetime
from typing import Any

import pytest
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from content.models.model_category import Category
from content.models.model_content import Content
from statistic.models import Statistic


class TestModelsStatistic:

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
        """ Создаем экземпляры модели Category, Content, get_user_model, Statistic"""
        user_object = get_user_model().objects.create_user(username='test_user',
                                                           email='test@example.com',
                                                           password='test_passwor123')

        category_object = Category.objects.create(name='Sport')

        content_object = Content.objects.create(title='Film',
                                                content=create_fake_video,
                                                description='description_film',
                                                pub_date_time=datetime.now(),
                                                author_content=user_object)

        content_object.categories_content.add(category_object)

        return Statistic.objects.create(content=content_object, author=user_object)

    def test_default_values(self, create_models: Statistic) -> None:
        """ Тестируем значения по умолчанию в модели Statistic"""
        assert create_models.number_of_likes == 0
        assert create_models.number_of_dislikes == 0
        assert create_models.number_of_comments == 0
        assert create_models.number_of_views == 0

    def test_foreign_keys(self, create_models: Statistic) -> None:
        """ Тестируем внешние ключи """
        assert str(create_models.author) == 'test_user'
        assert str(create_models.content) == 'Film'
