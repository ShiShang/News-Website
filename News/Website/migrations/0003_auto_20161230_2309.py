# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_auto_20161230_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='News',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.News', verbose_name='News'),
        ),
    ]