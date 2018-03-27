from uuid import uuid4

from django.db import models
from django_positions_2 import PositionManager, PositionField


class PositionManagedModel(models.Model):
    name = models.CharField(max_length=16, null=True, default=lambda: uuid4().hex)
    position = PositionField()
    objects = PositionManager()
