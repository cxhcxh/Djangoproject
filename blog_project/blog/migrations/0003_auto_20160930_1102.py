# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-30 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160929_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='\u4e2a\u4eba\u7f51\u9875\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
