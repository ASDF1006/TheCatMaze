# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20181128_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='riddle',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
    ]
