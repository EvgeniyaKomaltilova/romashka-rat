from datetime import datetime

from django.db import models


class New(models.Model):
    public = models.BooleanField('опубликовать', default=False)
    date = models.DateTimeField('дата публикации', default=datetime.now)
    text = models.CharField('текст новости', max_length=255)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.text[:50]


class Image(models.Model):
    public = models.BooleanField('опубликовать', default=False)
    name = models.CharField('название', max_length=127)
    picture = models.ImageField('фото', upload_to='images')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.name
