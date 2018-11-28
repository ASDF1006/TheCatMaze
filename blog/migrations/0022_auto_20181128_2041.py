# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20181128_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
