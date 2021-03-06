from datetime import datetime
from django.db import models
from romashka.services.naming import get_entry_name


class Entry(models.Model):
    """Модель записи на сайте"""

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Новости и контент'

    TOPICS = [
        ('news', 'новости'),
        ('about', 'о питомнике'),
        ('contract', 'договор'),
        ('varieties', 'разновидности'),
        ('colors', 'окрасы'),
        ('markings', 'маркировки')
    ]

    public = models.BooleanField(verbose_name='опубликовать', default=True)
    date = models.DateTimeField(verbose_name='дата добавления', default=datetime.now)
    topic = models.CharField(verbose_name='назначение', max_length=16, choices=TOPICS, null=True)
    title = models.CharField(verbose_name='заголовок', max_length=64, null=True)
    text = models.TextField(verbose_name='текст записи', max_length=2048)

    def __str__(self):
        return get_entry_name(self)
