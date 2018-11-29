# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('story', models.TextField(blank=True, null=True)),
                ('cat_image', models.ImageField(upload_to='cat/')),
                ('riddle', models.TextField(null=True)),
                ('riddle_image', models.ImageField(upload_to='riddle/')),
                ('hint', models.CharField(max_length=200, blank=True)),
                ('post_url', models.CharField(max_length=50, null=True)),
                ('next_url', models.CharField(max_length=50, null=True)),
                ('postProgress', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
