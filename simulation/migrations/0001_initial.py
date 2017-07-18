# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 09:38
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('opening_balance', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benchmark_year', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enterprises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start', models.DateField(blank=True, default=None, null=True)),
                ('termination', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('me', models.FloatField()),
                ('fme', models.FloatField()),
                ('erdp', models.FloatField()),
                ('dup', models.FloatField()),
                ('qm', models.FloatField()),
                ('maxInclusion', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('minInclusion', models.FloatField(null=True)),
                ('maxInclusion', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('start', models.DateField(blank=True, default=None, null=True)),
                ('termination', models.DateField(blank=True, default=None, null=True)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='simulation.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasesSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('quantity', models.FloatField()),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Enterprises')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='SalesSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('quantity', models.FloatField()),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Enterprises')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.PositiveIntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('day', models.PositiveSmallIntegerField()),
                ('precipitation', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('mean_vapour_pressure', models.FloatField()),
                ('mean_relative_humidity', models.FloatField()),
                ('sunshine', models.FloatField()),
                ('downward_diffuse_irradiation', models.FloatField()),
                ('direct_irradiation', models.FloatField()),
                ('potential_evapotranspiration', models.FloatField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='AccountsCreditor',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='simulation.Accounts')),
                ('credit_limit', models.FloatField(blank=True, default=None, null=True)),
                ('interest', models.FloatField(default=0)),
                ('max_delay', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsCurrent',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='simulation.Accounts')),
                ('overdraft_interest', models.FloatField(default=0)),
                ('credit_interest', models.FloatField(default=0)),
                ('overdraft_limit', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsDebitor',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='simulation.Accounts')),
                ('payment_delay', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountsLoans',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='simulation.Accounts')),
                ('interest', models.FloatField(default=0)),
                ('years_to_payback', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='payments',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming', to='simulation.Accounts'),
        ),
        migrations.AddField(
            model_name='payments',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing', to='simulation.Accounts'),
        ),
        migrations.AddField(
            model_name='goods',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario'),
        ),
        migrations.AddField(
            model_name='goods',
            name='units',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Units'),
        ),
        migrations.AddField(
            model_name='feedtypes',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario'),
        ),
        migrations.AddField(
            model_name='feeds',
            name='feed_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.FeedTypes'),
        ),
        migrations.AddField(
            model_name='feeds',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario'),
        ),
        migrations.AddField(
            model_name='enterprises',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Scenario'),
        ),
        migrations.AlterUniqueTogether(
            name='units',
            unique_together=set([('scenario', 'name')]),
        ),
        migrations.AddField(
            model_name='salessheet',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.AccountsDebitor'),
        ),
        migrations.AddField(
            model_name='purchasessheet',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.AccountsCreditor'),
        ),
        migrations.AlterUniqueTogether(
            name='goods',
            unique_together=set([('scenario', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='enterprises',
            unique_together=set([('scenario', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='accounts',
            unique_together=set([('scenario', 'name')]),
        ),
    ]
