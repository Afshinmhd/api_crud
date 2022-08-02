from django.db import models
from django.contrib.auth.models import User
from common.basemodel import BaseModel
from django.utils.translation import gettext as _


class MovieModel(BaseModel):
    """
        This class used to store movie information
    """
    title = models.CharField(_('title'), max_length=100)
    genre = models.CharField(_('genre'), max_length=100)
    creator = models.ForeignKey(User, verbose_name=_('creator'), on_delete=models.CASCADE)
    year = models.PositiveIntegerField(_('year'))

    class Meta:
        ordering = ['-id']
