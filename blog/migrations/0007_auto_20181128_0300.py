# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181127_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_url',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='prev_answer',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
