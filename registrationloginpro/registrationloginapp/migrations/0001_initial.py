# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-25 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]
