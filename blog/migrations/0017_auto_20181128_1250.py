# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20181128_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
