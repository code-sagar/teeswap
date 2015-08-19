# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tee', '0002_auto_20150819_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='tee',
            name='traded',
            field=models.BooleanField(default=False),
        ),
    ]
