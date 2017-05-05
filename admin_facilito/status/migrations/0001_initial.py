# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 05:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('activate', models.BooleanField(default=True)),
            ],
        ),
    ]
