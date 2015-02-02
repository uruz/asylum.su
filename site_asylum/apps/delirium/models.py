# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class DeliriumUser(models.Model):
    username = models.CharField('Имя пользователя', max_length=255, default='')
    avatar = models.CharField('Аватара', max_length=255, default='')

    class Meta:
        verbose_name = 'Пользователь Delirium'
        verbose_name_plural = 'Пользователи Delirium'


class Post(models.Model):
    topic = models.CharField('Топик', max_length=255, default='')
    posted_at = models.DateTimeField('Время')
    user = models.ForeignKey(DeliriumUser, related_name='posts', null=True, blank=True)
    is_registered = models.BooleanField('Зарегистрирован', default=False)
    username = models.CharField('Имя пользователя (в посте)', max_length=255, default='')
    text = models.TextField('Пост', default='')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
