# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20170418_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cederj_especifica1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='CEDERJ Espec\xedfica 1'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='cederj_especifica2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='CEDERJ Espec\xedfica 2'),
        ),
    ]
