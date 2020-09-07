from datetime import datetime
from django.db import models
from . import Rat


class Image(models.Model):
    date = models.DateTimeField(verbose_name='дата публикации', default=datetime.now)
    name = models.CharField(verbose_name='название', max_length=128)
    rat = models.ForeignKey(verbose_name='крыса', to='Rat', related_name='photos', on_delete=models.CASCADE,
                            null=True, blank=True)
    picture = models.ImageField(verbose_name='фото', upload_to='images')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.name
