from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from rest_framework.test import APITestCase
from rest_framework import status

from content.models.model_category import Category
from content.models.model_content import Content
from datetime import datetime


class YourModelTests(APITestCase):

    def create_fake_video(self) -> ContentFile:
        """ Создаем фикстуру ,которая будет создовать фейковый файл для поля content
            модели Content"""
        video_content = b'Video content'

        # Создаем ContentFile с заданным именем
        video_file = ContentFile(video_content, name='video.mp4')

        # Возвращаем объект ContentFile
        return video_file

    def setUp(self):
        """ Создаем экземпляр модели Category"""

        user_object = get_user_model().objects.create_user(username='test_user',
                                                           email='test@example.com',
                                                           password='test_passwor123')

        category_object = Category.objects.create(name='Cinema')

        content_object = Content.objects.create(title='Film',
                                                content=self.create_fake_video,
                                                description='description_film',
                                                pub_date_time=datetime.now(),
                                                author_content=user_object)

        content_object.categories_content.add(category_object)

    def test_content_list(self):
        response = self.client.get('api/content/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
