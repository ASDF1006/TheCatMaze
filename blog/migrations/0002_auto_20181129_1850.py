# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='postProgress',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='cat/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='riddle_image',
            field=models.ImageField(blank=True, upload_to='riddle/'),
        ),
    ]
