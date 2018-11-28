# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181128_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='prev_answer',
            new_name='next_url',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog/media/'),
        ),
    ]
