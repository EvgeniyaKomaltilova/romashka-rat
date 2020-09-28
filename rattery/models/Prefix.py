from django.db import models

from romashka.services.naming import get_prefix_name


class Prefix(models.Model):
    """Модель приставки питомника"""

    class Meta:
        verbose_name = 'Приставку'
        verbose_name_plural = 'Приставки питомников'

    female_name = models.CharField(verbose_name='приставка для самки', max_length=32)
    male_name = models.CharField(verbose_name='приставка для самца', max_length=32)
    suffix = models.BooleanField(verbose_name='после клички', default=True)

    def name(self):
        """Наименование приставки с учетом возможной разницы по полу крысенка"""
        return get_prefix_name(self)

    def __str__(self):
        return self.name()
