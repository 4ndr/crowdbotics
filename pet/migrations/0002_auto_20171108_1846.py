# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.Owner'),
        ),
    ]