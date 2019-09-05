# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-20 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190620_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Tag', verbose_name='博客标签'),
        ),
    ]