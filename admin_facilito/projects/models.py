from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models

from status.models import Status
from django.utils import timezone

import datetime

# Create your models here.


class Project(models.Model):
    user        = models.ForeignKey(User, on_delete= models.CASCADE)
    title       = models.CharField(max_length=50)
    description = models.TextField()
    dead_line   = models.DateField()
    create_date = models.DateField(default = datetime.date.today)
    slug        = models.CharField(max_length=50, default = "")  # Campo que se utiliza para obtener el registro de la base de datos

    def __str__(self):
        return self.title

    def validate_unique(self, exclude=None):
        self.slug = self.create_slug_field(self.title)
        if Project.objects.filter(slug = self.slug).exclude(pk = self.id).exists():
            raise ValidationError('Un proyecto con el mismo titulo ya se encuentra registrado')

    def create_slug_field(self, value):
        return value.lower().replace(" ", "-")


class ProjectStatus(models.Model):
    Project = models.ForeignKey(Project)
    status = models.ForeignKey(Status)
    create_date = models.DateTimeField(default=timezone.now)
