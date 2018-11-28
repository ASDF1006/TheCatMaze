# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181128_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
