# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name="person's first name")),
                ('last_name', models.CharField(max_length=150, unique=True, verbose_name="person's last name")),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='upload date')),
            ],
        ),
        migrations.AddField(
            model_name='cards',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uc_links.Person'),
        ),
    ]
