from django.db.models import fields
from posts.models import Blog
from likes.models import Like
from django.db import models
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType


class LikeSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField(read_only=True)
    updated_at = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"

    def create(self, validated_data):
        like = super(LikeSerializer, self).create(validated_data)
        like.content_type = ContentType.objects.get_for_model(Blog)
        like.user = self.context['request'].user
        like.save()
        return like


class LikeUpdateSerializer(serializers.ModelSerializer):
    updated_at = serializers.ReadOnlyField(read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = "__all__"




