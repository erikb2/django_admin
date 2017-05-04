from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

import datetime

# Create your models here.
class Project(models.Model):
    user        = models.ForeignKey(User, on_delete= models.CASCADE)
    title       = models.CharField(max_length=50)
    description = models.TextField()
    dead_line   = models.DateField()
    create_date = models.DateField(default = datetime.date.today)

    def __str__(self):
        return self.title
