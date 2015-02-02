# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliriumUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя', default='')),
                ('avatar', models.CharField(max_length=255, verbose_name='Аватара', default='')),
            ],
            options={
                'verbose_name_plural': 'Пользователи Delirium',
                'verbose_name': 'Пользователь Delirium',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('topic', models.CharField(max_length=255, verbose_name='Топик', default='')),
                ('posted_at', models.DateTimeField(verbose_name='Время')),
                ('is_registered', models.BooleanField(verbose_name='Зарегистрирован', default=False)),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя (в посте)', default='')),
                ('text', models.TextField(verbose_name='Пост', default='')),
                ('user', models.ForeignKey(blank=True, to='delirium.DeliriumUser', related_name='posts', null=True)),
            ],
            options={
                'verbose_name_plural': 'Посты',
                'verbose_name': 'Пост',
            },
            bases=(models.Model,),
        ),
    ]
