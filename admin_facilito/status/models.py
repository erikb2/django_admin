from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Status(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    color       = models.CharField(max_length=10)
    create_date = models.DateTimeField(default=timezone.now)
    activate    = models.BooleanField(default=True)

    @classmethod  # Para que sea un metodo de clase
    def get_default_status(cls):
        return cls.objects.get(pk=1)

    # Sirve para senalar como se nombrara el modelo en plural dentro del Admin
    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.title
