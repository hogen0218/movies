# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_details', '0003_movie_tail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tail',
            field=models.FileField(null=True, upload_to='vedio', verbose_name='预告片'),
        ),
    ]
