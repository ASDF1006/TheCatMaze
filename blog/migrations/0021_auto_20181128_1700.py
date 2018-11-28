# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_post_hint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='next_url',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_url',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
