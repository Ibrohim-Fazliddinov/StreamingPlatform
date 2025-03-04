<<<<<<< HEAD
from api.views import api_root_view
from accounts.urls import urlpatterns as auth_api
from content.urls import urlpatterns as content_api
from django.urls import path, include

app_name = 'api'


urlpatterns = [
    path('',api_root_view, name='api-root'),
    path('auth/', include('djoser.urls.jwt')),
]



=======
from api.spectacular.urls import urlpatterns as doc_api
from users.urls import urlpatterns as auth_api
app_name = 'api'


urlpatterns = []
urlpatterns += doc_api
>>>>>>> auth
urlpatterns += auth_api
urlpatterns += content_api