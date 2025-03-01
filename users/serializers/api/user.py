# from django.db import transaction
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.exceptions import ParseError
# from phonenumber_field.serializerfields import PhoneNumberField
#
# from users.serializers.nested.profile import ProfileShortSerializer, ProfileUpdateSerializer
#
# User = get_user_model()
# # region ------------------- AUTHENTICATION AND AUTHORISATION -------------------
# class RegistrationSerializer(serializers.ModelSerializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField(
#         style={'input_type': 'password'},
#         write_only=True
#     )
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     telephone = PhoneNumberField(
#         required=False,
#         write_only=True,
#     )
#
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'telephone',
#             'password',
#
#         )
#
#     def validate(self, attrs):
#         email = attrs['email'].lower()
#         username = attrs['username']
#         if User.objects.filter(email=email).exists():
#             raise ParseError('Пользователь с такой почтой уже зарегистрирован.')
#         if User.objects.filter(username=username).exists():
#             raise ParseError('Пользователь с таким именем уже зарегистрирован.')
#         return attrs
#
#     def validate_password(self, value):
#         validate_password(value)
#         return value
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = User.objects.create_user(**validated_data)
#         user.set_password(password)  # Хеширование пароля
#         user.save()
#         return user
#
# # endregion ---------------------------------------------------------------------
#
# # region ------------------- PASSWORD CHANGING -----------------------------------
#
# class ChangePasswordSerializer(serializers.ModelSerializer):
#     old_password = serializers.CharField(write_only=True)
#     new_password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('old_password', 'new_password',)
#
#     def validate(self, attrs):
#         user = self.instance
#         old_password = attrs.pop('old_password')
#         if not user.check_password(old_password):
#             raise ParseError(
#                 'Проверьте правильность старого пароля'
#             )
#         return attrs
#
#     def validate_new_password(self, value):
#         validate_password(value)
#         return value
#
#     def update(self, instance, validated_data):
#         password = validated_data.pop('new_password')
#         instance.set_password(password)
#         instance.save()
#         return instance
#
# # endregion ---------------------------------------------------------------------------
#
# # region ------------------- USER (USER_UPDATE) AND PROFILE SERIALIZERS ----------------------
#
#
# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileShortSerializer()
#
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = (
#             'id',
#             'username',
#             'email',
#             'first_name',
#             'last_name',
#             'telephone',
#             'profile',
#             'created_at',
#         )
#
#
# class UserUpdateSerializer(serializers.ModelSerializer):
#     profile = ProfileUpdateSerializer()
#
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#             'first_name',
#             'last_name',
#             'telephone',
#             'profile',
#         )
#
#     def update(self, instance, validated_data):
#         # Проверка наличия профиля
#         profile_data = validated_data.pop('profile') if 'profile' in validated_data else None
#         with transaction.atomic():
#             instance = super().update(instance, validated_data)
#
#         # Update профиля
#         self._update_profile(profile=instance.profile, data=profile_data)
#         return instance
#
#     def _update_profile(self, profile, data):
#         profile_serializer = ProfileUpdateSerializer(
#             instance=profile, data=data, partial=True
#         )
#         profile_serializer.is_valid(raise_exception=True)
#         profile_serializer.save()
#
# # endregion --------------------------------------------------------------------
