# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNP', '0007_auto_20160511_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snp',
            name='reference',
            field=models.CharField(default='NONE', max_length=255),
        ),
    ]
