from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Status(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    color       = models.CharField(max_length = 10)
    create_date = models.DateTimeField(default = timezone.now)
    activate    = models.BooleanField(default = True)

    # Sirve para senalar como se nombrara el modelo en plural dentro del Admin
    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.title
