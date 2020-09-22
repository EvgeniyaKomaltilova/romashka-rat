from datetime import date
from django.db import models

from romashka.services.litters_string import get_litters_as_string
from romashka.services.photo import get_main_photo
from romashka.services.status import get_status_based_on_gender
from romashka.services.timedelta import get_rat_lifespan, get_rat_current_age
from romashka.services.naming import get_full_rat_name
from romashka.services.absolute_urls import get_rat_url


class Rat(models.Model):

    GENDER = [
        ('male', 'самец'),
        ('female', 'самка')
    ]

    TITLE = [
        ('none', 'без титула'),
        ('champion', 'чемпион'),
        ('grandchampion', 'грандчемпион')
    ]

    STATUS = [
        ('available', 'свободен'),
        ('reserved', 'зарезервирован'),
        ('owned', 'у владельца')
    ]

    old_id = models.PositiveSmallIntegerField(verbose_name='старый id', null=True, blank=True)
    public = models.BooleanField(verbose_name='опубликовать', default=True)
    alive = models.BooleanField(verbose_name='жив(а)', default=True)
    in_rattery = models.BooleanField(verbose_name='производитель', default=False)
    castrate = models.BooleanField(verbose_name='кастрирован(а)', default=False)
    status = models.CharField(verbose_name='статус', max_length=16, choices=STATUS, default='owned')
    litter = models.ForeignKey(verbose_name='литера', to='Litter', related_name='children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    date_of_add = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)
    name = models.CharField(verbose_name='кличка', max_length=32)
    prefix = models.ForeignKey(verbose_name='приставка', to='Prefix', related_name='rats',
                               on_delete=models.SET_NULL, null=True, blank=True)
    variety = models.CharField(verbose_name='разновидность', max_length=128)
    gender = models.CharField(verbose_name='пол', max_length=8, choices=GENDER, default='male')
    title = models.CharField(verbose_name='титул', max_length=16, choices=TITLE, default='none')
    date_of_birth = models.DateField(verbose_name='дата рождения', default=date.today)
    date_of_death = models.DateField(verbose_name='дата смерти', default=None, null=True, blank=True)
    breeder = models.ForeignKey(verbose_name='заводчик', to='Person', related_name='rats_bred',
                                on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(verbose_name='владелец', to='Person', related_name='rats_own', on_delete=models.SET_NULL,
                              null=True, blank=True)
    father = models.ForeignKey(verbose_name='отец', to='self', related_name='father_children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    mother = models.ForeignKey(verbose_name='мать', to='self', related_name='mother_children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    information = models.TextField(verbose_name='информация', max_length=2048, null=True, blank=True)

    class Meta:
        verbose_name = 'крысу'
        verbose_name_plural = 'Крысы'

    def save(self, *args, **kwargs):
        """изменение базовых правил сохранения крысы"""
        # если крыса добавляется из админки "литеры", то ей присваиваются значения полей литеры
        if self.litter:
            self.date_of_birth = self.litter.date_of_birth
            self.prefix = self.litter.prefix
            self.mother = self.litter.mother
            self.father = self.litter.father
            self.breeder = self.litter.breeder
        # если у крысы есть дата смерти, она считается мертвой
        if self.date_of_death:
            self.alive = False
        # если со дня рождения крысы прошло больше 4х лет, она считается мертвой
        if (date.today() - self.date_of_birth).total_seconds() > 126144000:
            self.alive = False
        super(Rat, self).save(*args, **kwargs)

    def main_photo(self):
        return get_main_photo(self)

    def status_based_on_gender(self):
        return get_status_based_on_gender(self)

    def full_name(self):
        return get_full_rat_name(self)

    def lifespan(self):
        return get_rat_lifespan(self)

    def current_age(self):
        return get_rat_current_age(self)

    def litters(self):
        return get_litters_as_string(self)

    def url(self):
        return get_rat_url(self)

    def __str__(self):
        return self.full_name()
