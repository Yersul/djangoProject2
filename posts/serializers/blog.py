from rest_framework import serializers

from comment.models import Comment
from comment.serializers import CommentSerializer,  CommentUUIDSerializer
from posts.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    # comments = CommentUUIDSerializer(required=False, many=True, )
    comments = serializers.SerializerMethodField(method_name='get_comments')

    class Meta:
        model = Blog
        fields = (
            'uuid',
            'titles',
            'text',
            'author',
            'comments',
            'post_kind',
            # 'is_moderated',
        )
        read_only_fields = ('created_at', 'updated_at')

    # def _get_children(self, comment_id):
    #     children = ChildDetailSerializer(Child.objects.filter(comment_id=comment_id), many=True)
    #     return children
    #

    def get_comments(self, obj):
        comments = obj.comments.filter(parent=None)
        serializer = CommentUUIDSerializer(comments, many=True)
        return serializer.data


class BlogCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = (
            'uuid',
            'titles',
            'text',
            'author',
            'post_kind',
            # 'is_moderated',
        )
        read_only_fields = ('created_at', 'updated_at')


class BlogDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogModerateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'uuid',
            'titles',
            'text',
            'post_kind',
            'is_moderated',
        )
