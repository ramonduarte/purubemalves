# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_redacao', '0004_tema_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
