from datetime import date
from django.db import models
from romashka.services.naming import get_full_litter_name, get_litter_name_for_admin
from romashka.services.absolute_urls import get_litter_url


class Litter(models.Model):
    """Модель помета (выводка, литеры)"""

    class Meta:
        verbose_name = 'Литеру'
        verbose_name_plural = 'Литеры'

    public = models.BooleanField(verbose_name='опубликовать', default=True)
    name = models.CharField(verbose_name='название', max_length=8)
    prefix = models.ForeignKey(verbose_name='приставка', to='Prefix', related_name='litters',
                               on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(verbose_name='номер', max_length=16, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='дата рождения', default=date.today)
    year = models.CharField(verbose_name="год рождения", max_length=4, default=date.today().year)
    father = models.ForeignKey(verbose_name='отец', to='Rat', related_name='father_litters', on_delete=models.SET_NULL,
                               null=True, blank=True)
    mother = models.ForeignKey(verbose_name='мать', to='Rat', related_name='mother_litters', on_delete=models.SET_NULL,
                               null=True, blank=True)
    breeder = models.ForeignKey(verbose_name='заводчик', to='Person', related_name='litters', on_delete=models.SET_NULL,
                                null=True, blank=True)

    def full_name(self):
        """Название помета с приставкой питомника"""
        return get_full_litter_name(self)

    def url(self):
        """URL литеры с учетом года рождения"""
        return get_litter_url(self)

    def __str__(self):
        return get_litter_name_for_admin(self)
