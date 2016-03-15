# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-15 19:36
from __future__ import unicode_literals

import arche.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Odp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.CharField(max_length=3)),
                ('tresc', models.TextField(null=True)),
                ('rodzajOdpowiedzi', models.CharField(choices=[('TF', 'Prawda albo fa\u0142sz'), ('5S', '5-stopniowa')], max_length=2)),
                ('klasyfikacja', models.CharField(choices=[('ICD-10', 'ICD-10'), ('DSM-IV', 'DSM-IV'), ('DSM-5', 'DSM-5')], max_length=6)),
                ('grupa', models.IntegerField(null=True)),
                ('choroba', models.TextField()),
                ('id_pytania', models.IntegerField(null=True)),
                ('odpowiedz', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Opis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pytanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.CharField(max_length=3)),
                ('tresc', models.TextField()),
                ('rodzajOdpowiedzi', models.CharField(choices=[('TF', 'Prawda albo fa\u0142sz'), ('5S', '5-stopniowa')], max_length=2)),
                ('klasyfikacja', models.CharField(choices=[('ICD-10', 'ICD-10'), ('DSM-IV', 'DSM-IV'), ('DSM-5', 'DSM-5')], max_length=6)),
                ('grupa', models.IntegerField(null=True)),
                ('choroba', models.TextField()),
                ('opis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arche.Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('student', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsernameEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ZmianaHasla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=21)),
                ('password', models.CharField(max_length=30, validators=[arche.models.validate_password])),
            ],
        ),
        migrations.AddField(
            model_name='odp',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arche.Quiz'),
        ),
    ]
