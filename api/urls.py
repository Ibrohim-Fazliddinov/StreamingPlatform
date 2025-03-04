from api.spectacular.urls import urlpatterns as doc_api
from users.urls import urlpatterns as auth_api
app_name = 'api'


urlpatterns = []
urlpatterns += doc_api
urlpatterns += auth_api
