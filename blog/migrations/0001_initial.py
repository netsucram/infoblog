# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('text', models.TextField(verbose_name='Texto')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Criação')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de Publicação')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
        ),
    ]
