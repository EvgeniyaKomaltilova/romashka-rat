from django.db import models
from romashka.services.naming import get_person_short_name, get_person_full_name


class Person(models.Model):
    """Модель персоны (заводчик/владелец)"""

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Заводчики и владельцы'

    last_name = models.CharField(verbose_name='фамилия', max_length=32)
    first_name = models.CharField(verbose_name='имя', max_length=32)
    second_name = models.CharField(verbose_name='отчество', max_length=32, null=True, blank=True)
    location = models.ForeignKey(verbose_name='место проживания', to='Location', related_name='persons',
                                 on_delete=models.SET_NULL, null=True)

    def full_name(self):
        """Полное имя: фамилия, имя и отчество"""
        return get_person_full_name(self)

    def short_name(self):
        """Сокращенное имя: фамилия и инициалы"""
        return get_person_short_name(self)

    def __str__(self):
        return get_person_short_name(self)
