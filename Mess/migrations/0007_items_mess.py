# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0006_extras_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='mess',
            field=models.CharField(default='A', max_length=2),
        ),
    ]