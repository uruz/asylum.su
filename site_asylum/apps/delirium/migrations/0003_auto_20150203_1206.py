# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delirium', '0002_auto_20150202_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliriumuser',
            options={'ordering': ('id',), 'verbose_name_plural': 'Пользователи Delirium', 'verbose_name': 'Пользователь Delirium'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id',), 'verbose_name_plural': 'Посты', 'verbose_name': 'Пост'},
        ),
    ]
