# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 06:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngaraapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(default='SOME STRING', max_length=30)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='index',
            name='context',
        ),
        migrations.AddField(
            model_name='index',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='index',
            name='service',
            field=models.CharField(default='General cleaning', max_length=30),
        ),
    ]
