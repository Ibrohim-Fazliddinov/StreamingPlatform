from django.urls import path, include
from users.serializers.views import users
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('users/reg', users.RegistrationView.as_view(), name='reg'),
    # path('users/profile', users.ProfileView.as_view(), name='profile'),
    # path('users/change-password', users.ChangePasswordView.as_view(), name='change-password'),
]
urlpatterns += [
    # Маршруты для работы с dj-rest-auth
    path('auth/', include('dj_rest_auth.urls')),

    # # Маршруты для шаблонов Django
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]