# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_auto_20170807_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg.Party'),
        ),
    ]
