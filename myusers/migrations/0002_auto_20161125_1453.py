# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-25 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='IDcard',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='MBDA',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='MBWT',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='QQ',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='retryCount',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='token',
        ),
    ]