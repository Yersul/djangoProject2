from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'phone',
            'first_name',
            'last_name',
            'created_at',
            'updated_at'
        )
