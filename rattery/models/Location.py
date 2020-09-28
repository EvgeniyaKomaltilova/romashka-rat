from django.db import models


class Location(models.Model):
    """Модель локации (месторасположения)"""

    class Meta:
        verbose_name = 'Локацию'
        verbose_name_plural = 'Локации'

    country = models.CharField(verbose_name='страна', max_length=32)
    region = models.CharField(verbose_name='регион', max_length=322, null=True)
    city = models.CharField(verbose_name='населенный пункт', max_length=32)

    def __str__(self):
        return f'{self.city}, {self.country}'
