# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
