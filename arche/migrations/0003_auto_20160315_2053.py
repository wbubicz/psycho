# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-15 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arche', '0002_formularzchcezmianyhasla'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormularzChceZmianyHasla',
            new_name='ChceZmianyHasla',
        ),
    ]