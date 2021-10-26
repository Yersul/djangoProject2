from django.db import models

from posts.models import Blog
from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Comment(AbstractUUID, AbstractTimeTracker):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='childs')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    comment = models.TextField(verbose_name='коммент')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='comments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
