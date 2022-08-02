from django.db import models
from django.utils.translation import gettext as _


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    
class BaseModel(models.Model):
    is_created = models.DateTimeField(_('is_created'), auto_now_add=True)
    is_updated = models.DateTimeField(_('is_updated'), auto_now=True)
    is_deleted = models.BooleanField(_('is_deleted'), default=False)

    objects = BaseManager()

    class Meta:
        abstract = True