# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0011_auto_20170828_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currentaccount',
            options={'verbose_name': 'Customer Account', 'verbose_name_plural': 'Accounts-Current'},
        ),
        migrations.AlterModelOptions(
            name='customeraccount',
            options={'verbose_name': 'Customer Account', 'verbose_name_plural': 'Accounts-Customer'},
        ),
        migrations.AlterModelOptions(
            name='loanaccount',
            options={'verbose_name': 'Loan', 'verbose_name_plural': 'Accounts-Loan'},
        ),
        migrations.AlterModelOptions(
            name='supplieraccount',
            options={'verbose_name': 'Supplier Account', 'verbose_name_plural': 'Accounts-Supplier'},
        ),
        migrations.AddField(
            model_name='scenario',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
