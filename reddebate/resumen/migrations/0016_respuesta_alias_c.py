# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-21 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumen', '0015_auto_20161221_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='alias_c',
            field=models.CharField(default='username', max_length=50),
        ),
    ]