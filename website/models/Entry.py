from datetime import datetime
from django.db import models


class Entry(models.Model):

    TOPICS = [
        ('news', 'новости'),
        ('about', 'о питомнике'),
        ('varieties', 'разновидности')
    ]

    public = models.BooleanField(verbose_name='опубликовать', default=True)
    date = models.DateTimeField(verbose_name='дата добавления', default=datetime.now)
    topic = models.CharField(verbose_name='назначение', max_length=16, choices=TOPICS, null=True)
    title = models.CharField(verbose_name='заголовок', max_length=64, null=True)
    text = models.TextField(verbose_name='текст записи', max_length=2048)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Новости и контент'

    def __str__(self):
        return f'{self.topic}: {self.title}'


