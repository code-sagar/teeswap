# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tee',
            name='qid',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
