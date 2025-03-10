from django.urls import path, include
from rest_framework import routers

from content.api.views.content_view_set import ContentViewSet
from content.api.views.elasticsearch_view import ElasticsearchView

app_name = 'content'

router = routers.SimpleRouter()
router.register(r'content', ContentViewSet, basename='content')


urlpatterns = [
    path('', include(router.urls)),
    path('search/', ElasticsearchView.as_view(), name='search')
]
