# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('full_name', models.CharField(default=b'', max_length=130)),
                ('email', models.EmailField(unique=True, max_length=254, db_index=True)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateField(default=None, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('city', models.CharField(default=None, max_length=31, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
