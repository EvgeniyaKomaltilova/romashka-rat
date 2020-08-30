from datetime import datetime

from django.db import models


class New(models.Model):
    date = models.DateTimeField(default=datetime.now)
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.text[:50]