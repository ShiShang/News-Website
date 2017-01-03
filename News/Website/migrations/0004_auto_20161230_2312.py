# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20161230_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Author',
        ),
        migrations.AlterField(
            model_name='author',
            name='News',
            field=models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.News', verbose_name='News'),
        ),
    ]