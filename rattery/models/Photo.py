from datetime import datetime
from django.db import models


class Photo(models.Model):
    """Модель фотографии крысы"""

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    date = models.DateTimeField(verbose_name='дата публикации', default=datetime.now)
    name = models.CharField(verbose_name='название', max_length=128)
    rat = models.ForeignKey(verbose_name='крыса', to='Rat', related_name='photos', on_delete=models.CASCADE,
                            null=True, blank=True)
    picture = models.ImageField(verbose_name='фото', upload_to='photos')

    def __str__(self):
        return self.name
