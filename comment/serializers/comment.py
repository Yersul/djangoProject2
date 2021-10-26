from django.http import Http404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from comment.models import Comment


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    childs = CommentChildSerializer(required=False, many=True)

    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'comment',
            'author',
            'childs',
        )

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post',
            'comment',

        )
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        post = validated_data.pop('post', None)

        if post:
            instance = Comment.objects.create(**validated_data)
            return instance


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post'
            'comment',
            'updated_at',
        )


class CommentUUIDSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(required=True)
    comment = serializers.UUIDField(required=False)

    class Meta:
        model = Comment
        fields = (
            'uuid',
            'comment'
        )



