# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SNP', '0003_snp_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snp',
            name='reference',
        ),
    ]
