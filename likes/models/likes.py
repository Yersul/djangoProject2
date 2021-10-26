from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from posts.models import Blog
from users.models import CustomUser
from utils.const import LikeKindChoice
from utils.models import AbstractUUID, AbstractTimeTracker


class Like(AbstractUUID, AbstractTimeTracker):
    post = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='likes',
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Хозяин',
        related_name='likes',
    )

    kind = models.CharField(
        choices=LikeKindChoice.choice(),
        max_length=8,
        blank=True,
        null=True,
        verbose_name='Like Type'
    )

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.owner.last_name)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ('post', 'owner')

# post = Post.objects.get(uuid = abvgd)
# likes = post.likes.filter(kind = 'LIKE').count()