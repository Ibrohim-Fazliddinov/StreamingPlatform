from datetime import datetime
import string
from typing import Any

import pytest
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db import IntegrityError

from .models.model_category import Category
from .models.model_content import Content
from .services import slug_generation


@pytest.mark.parametrize("size_slug,result", [
    (150, 150),
    (200, 200),
    (250, 250)
])
def test_slug_generation(size_slug: int, result: int) -> None:
    """ Проверяем, что длина возвращаемого слага соответствует переданным значениям в аргументах функции """
    assert len(slug_generation(size_slug)) == result


@pytest.mark.parametrize("size_slug,count_slug", [
    (150, 150),
    (200, 200),
    (250, 250)
])
def test_slug_unique(size_slug: int, count_slug: int) -> None:
    """ Проверяем функциию на уникальность возвращаемых значений """
    generated_slug_list = [slug_generation(size_slug) for _ in range(count_slug)]
    assert len(set(generated_slug_list)) == count_slug


def test_slug_occurrence_symbol() -> None:
    """ Проверяем ,что в слаг входят только разрешенные символы """
    all_symbols = string.ascii_uppercase + string.digits
    iterator_slug = (slug_generation(150) for _ in range(100))

    for slug in iterator_slug:
        for symbol in slug:
            assert symbol in all_symbols


class TestModelsCategory:

    @pytest.fixture
    def create_models(self, db: Any) -> Category:
        """ Создаем экземпляр модели Category"""

        return Category.objects.create(name='Cinema')

    def test_category_exists(self, create_models: Category) -> None:
        """ Проверяем создалась ли запись"""
        assert Category.objects.filter(name='Cinema').exists()

    def test_update_category(self, create_models: Category) -> None:
        """ Проверяем экземпляр модели Category на предмет изменения"""
        create_models.name = 'Sport'
        create_models.save()
        update_category = Category.objects.get(name='Sport')
        assert update_category.name == 'Sport'

    def test_unique_category(self, create_models: Category) -> None:
        """ Проверяем экземпляр модели Category на уникальность поля name"""
        with pytest.raises(IntegrityError):
            Category.objects.create(name='Cinema')
        assert True


class TestModelsContent:
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

        category_object = Category.objects.create(name='Sport')

        content_object = Content.objects.create(title='Film',
                                                content=create_fake_video,
                                                description='description_film',
                                                pub_date_time=datetime.now(),
                                                author_content=user_object)

        content_object.categories_content.add(category_object)

        return content_object

    def test_content_slug(self, create_models: Content) -> None:
        """ Проверяем добовление переопределенным методом save модели Content уникального слага"""
        assert len(create_models.slug) == 150
        assert create_models.slug != ''

    def test_update_content(self, create_models: Content) -> None:
        """ Проверяем экземпляр модели Content на предмет изменения поля title"""
        create_models.title = 'Mult'
        create_models.save()
        update_content_title = Content.objects.get(title='Mult')
        assert update_content_title.title == 'Mult'

    def test_foreign_keys_content(self, create_models: Content) -> None:
        assert str(create_models.author_content) == 'test_user'
