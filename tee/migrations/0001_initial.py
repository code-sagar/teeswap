# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('qid', models.CharField(max_length=255, null=True)),
                ('havecolor', models.CharField(max_length=10, null=True)),
                ('traded', models.BooleanField(default=False)),
                ('havesize', models.ForeignKey(related_name='havesize', to='tee.Size', null=True)),
                ('wantsize', models.ForeignKey(related_name='wantsize', to='tee.Size', null=True)),
            ],
        ),
    ]
