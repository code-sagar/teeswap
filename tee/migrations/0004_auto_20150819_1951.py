# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tee', '0003_tee_traded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('size', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tee',
            name='havesize',
            field=models.ForeignKey(to='tee.Size', null=True, related_name='havesize'),
        ),
        migrations.AlterField(
            model_name='tee',
            name='wantsize',
            field=models.ForeignKey(to='tee.Size', null=True, related_name='wantsize'),
        ),
    ]
