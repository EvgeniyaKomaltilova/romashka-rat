from datetime import datetime
from django.db import models


class Image(models.Model):
    """Модель изображения для иллюстрации записей"""

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    main_page = models.BooleanField(verbose_name='на главной странице', default=False)
    date = models.DateTimeField(verbose_name='дата публикации', default=datetime.now)
    name = models.CharField(verbose_name='название', max_length=128)
    entry = models.ForeignKey(verbose_name='запись', to='Entry', related_name='images', on_delete=models.CASCADE,
                              null=True, blank=True)
    picture = models.ImageField(verbose_name='фото', upload_to='images')

    def __str__(self):
        return self.name
