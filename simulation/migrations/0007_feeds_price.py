# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0006_auto_20170815_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]