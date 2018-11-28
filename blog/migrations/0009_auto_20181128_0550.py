# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='progress',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='progress',
            name='title',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
