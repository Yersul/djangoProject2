from uuid import uuid4
from django.db import models


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        verbose_name="uuid"
    )

    class Meta:
        abstract = True
        ordering = ('uuid', )


class AbstractTimeTracker(models.Model):
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_at'
    )

    class Meta:
        abstract = True
        ordering = ('updated_at', 'created_at')
