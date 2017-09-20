# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 01:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uc_links', '0002_auto_20170920_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_number',
            field=models.CharField(max_length=4, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4}\\d$')]),
        ),
    ]