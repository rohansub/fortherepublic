# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-21 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_issue_upvoters'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='message',
            field=models.CharField(default='', max_length=100),
        ),
    ]
