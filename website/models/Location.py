from django.db import models


class Location(models.Model):
    country = models.CharField(verbose_name='страна', max_length=32)
    city = models.CharField(verbose_name='город', max_length=32)

    class Meta:
        verbose_name = 'локацию'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'{self.city}, {self.country}'
