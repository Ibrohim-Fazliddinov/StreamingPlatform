from rest_framework import serializers
from users.models.profile import Profile


class ProfileShortSerializer(serializers.ModelSerializer):
    """Вложенный сериализатор профиля"""

    class Meta:
        model = Profile
        fields = (
            'user_photo',
            'description',
        )

class ProfileUpdateSerializer(serializers.ModelSerializer):
    """Вложенный сериализатор обновления профиля"""

    class Meta:
        model = Profile
        fields = (
            'user_photo',
            'description',
        )
