# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 02:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie_details', '0002_auto_20181102_0844'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_details.Movie', verbose_name='评论的电影')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论的用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
