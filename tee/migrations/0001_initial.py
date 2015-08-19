# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('qid', models.CharField(max_length=255, null=True, unique=True)),
                ('havesize', models.CharField(max_length=3, null=True)),
                ('wantsize', models.CharField(max_length=3, null=True)),
                ('havecolor', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
