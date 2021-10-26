from rest_framework import serializers

from comment.models import Comment
from comment.serializers import CommentSerializer,  CommentUUIDSerializer
from posts.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentUUIDSerializer(required=False, many=True)

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
    # def add_comment(self, post_id):
    #     comments = Comment.objects.filter(post_id=post_id)
    #     comments = CommentSerializer(comments, many=True)
    #     for comment in comments:
    #         comment['children'] = self._get_children(comment['uuid'])
    #     return comments


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
