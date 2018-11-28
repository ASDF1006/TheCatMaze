# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_delete_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat_image',
            field=models.ImageField(upload_to='cat/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='riddle_image',
            field=models.ImageField(upload_to='riddle/'),
        ),
    ]
