# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import os

from django.conf import settings
from django.db import models, migrations
from django.utils.timezone import make_aware
import phpserialize
import pytz

def forwards_func(apps, schema_editor):
    if not hasattr(settings, 'IMPORT_DELIRIUM'):
        return
    Post = apps.get_model('delirium', 'Post')
    User = apps.get_model('delirium', 'DeliriumUser')
    User.objects.all().delete()
    Post.objects.all().delete()
    db_alias = schema_editor.connection.alias
    path = os.path.join(settings.BASE_DIR, 'data', 'asylum', 'files')
    filenames = [filename for filename in os.listdir(path) if filename.startswith('delirium_') and filename.endswith('.txt')]
    filenames.sort(key = lambda filename: int(filename.split('.')[0].split('_')[1]))
    for filename in filenames:
        with open(os.path.join(path, filename), 'rb') as postfile:
            data = postfile.read().decode('utf-8').encode('windows-1251')
            bytesdict = phpserialize.loads(data)
            unidict = {}
            kwargs = {}
            for key, value in bytesdict.items():
                unidict[key.decode('windows-1251')] = value.decode('windows-1251')
            if unidict['user_reg']:
                user, _ = User.objects.get_or_create(username = unidict['realusername'],
                                                     defaults = {'avatar': unidict['user_avatar']})
                kwargs['user'] = user
            posted_at = datetime.strptime(unidict['time'], '%d.%m.%Y %H:%M')
            moscow = pytz.timezone('Europe/Moscow')
            try:
                aware = make_aware(posted_at, moscow)
            except pytz.exceptions.AmbiguousTimeError:
                aware = moscow.localize(posted_at, is_dst=True)
            kwargs.update({
                'topic': unidict['topic'],
                'username': unidict['user_name'],
                'posted_at': aware,
                'is_registered': unidict['user_reg'],
                'text': unidict['post']
            })
            Post.objects.create(**kwargs)


class Migration(migrations.Migration):

    dependencies = [
        ('delirium', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func)
    ]
