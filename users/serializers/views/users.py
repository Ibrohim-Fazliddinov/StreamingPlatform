# from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
# from django.contrib.auth import get_user_model
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from drf_spectacular.utils import extend_schema_view, extend_schema
# from rest_framework import status
# from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.status import HTTP_204_NO_CONTENT
# from users.serializers.api import user as user_s
#
# User = get_user_model()
#
#
# @extend_schema_view(
#     post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация и Авторизация'])
# )
# class RegistrationView(CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     serializer_class = user_s.RegistrationSerializer
#
#
# @extend_schema_view(
#     post=extend_schema(
#         request=user_s.ChangePasswordSerializer, summary='Смена пароля', tags=['Аутентификация и Авторизация'])
# )
# class ChangePasswordView(APIView):
#
#     def post(self, request):
#         user = request.user
#         serializer = user_s.ChangePasswordSerializer(
#             instance=user, data=request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=HTTP_204_NO_CONTENT)  # 204 - мы все обработали все(все хорошо) но ничего не возращаем
#
#
# @extend_schema_view(
#     get=extend_schema(summary='Получения <Профиля пользователя>', tags=['Профили Пользователей']),
#     put=extend_schema(summary='Изменение <Профиля пользователя>', tags=['Профили Пользователей']),
#     patch=extend_schema(summary='Частичное изменения <Профиля пользователя>', tags=['Профили Пользователей'])
# )
# class ProfileView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = user_s.UserSerializer
#     http_method_names = ('get', 'patch')
#
#     def get_serializer_class(self):
#         if self.request.method in ['PUT', 'PATCH']:
#             return user_s.UserUpdateSerializer
#         return user_s.UserSerializer
#
#     def get_object(self):
#         return self.request.user
#

