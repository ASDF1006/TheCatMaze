# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181128_0553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='progress',
            new_name='postProgress',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='recent_progress',
            new_name='dbProgress',
        ),
    ]
