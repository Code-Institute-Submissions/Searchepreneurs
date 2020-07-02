# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-02 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20200702_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='last_edited',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
