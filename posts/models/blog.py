from django.utils.translation import ugettext_lazy as _
from django.db import models

from users.models import CustomUser
from utils.const import PostKindChoice
from utils.models import AbstractTimeTracker, AbstractUUID


class Blog(AbstractUUID, AbstractTimeTracker):
    titles = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Владелец поста',
    )

    post_kind = models.CharField(
        choices=PostKindChoice.choice(),
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Тип поста'
    )
    is_moderated = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        order_with_respect_to = 'author'

    def __str__(self):
        return self.titles


