from django.db import models

from django.utils import timezone


class DBmodel(models.Model):

    """same field"""

    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.UUIDField(null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.UUIDField(null=True)
    is_activate = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True
