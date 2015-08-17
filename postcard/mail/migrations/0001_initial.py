# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=127)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('mail', models.ForeignKey(to='mail.Mail')),
            ],
        ),
        migrations.CreateModel(
            name='UserThreadMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery_status', models.CharField(max_length=4, choices=[(b'CC', b'CC'), (b'BCC', b'BCC'), (b'TO', b'TO'), (b'FROM', b'FROM')])),
                ('thread', models.ForeignKey(to='mail.Thread')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='thread',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='mail.UserThreadMap'),
        ),
    ]
