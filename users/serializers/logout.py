from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=1000, required=True)

    class Meta:
        fields = (
            'refresh',
        )

    def validate(self, attrs):
        if 'refresh' not in attrs.keys():
            raise ValidationError('refresh token is not found')

        return attrs
