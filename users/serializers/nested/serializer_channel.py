from rest_framework import serializers
from channel.models import Channel


class ChannelShortSerializer(serializers.ModelSerializer):
    """Вложенный сериализатор channel"""

    class Meta:
        model = Channel
        fields = (
            'title',
            'description',
            'channel_photo'
        )


class ChannelUpdateSerializer(serializers.ModelSerializer):
    """Вложенный сериализатор обновления Channel"""

    class Meta:
        model = Channel
        fields = (
            'title',
            'description',
            'channel_photo'
        )
