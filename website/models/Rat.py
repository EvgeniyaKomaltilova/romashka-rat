from datetime import datetime, date, timedelta
from django.db import models
from website.services.get_timedelta_as_string import get_timedelta_as_string
from . import Prefix, Person, Litter


class Rat(models.Model):

    GENDER = [
        ('самец', 'самец'),
        ('самка', 'самка')
    ]

    TITLE = [
        ('нет', 'без титула'),
        ('чемпион', 'чемпион'),
        ('грандчемпион', 'грандчемпион')
    ]

    STATUS = [
        ('свободен', 'свободен'),
        ('зарезервирован', 'зарезервирован'),
        ('у владельца', 'у владельца')
    ]

    public = models.BooleanField(verbose_name='опубликовать', default=True)
    alive = models.BooleanField(verbose_name='жив(а)', default=True)
    in_rattery = models.BooleanField(verbose_name='производитель', default=False)
    castrate = models.BooleanField(verbose_name='кастрирован(а)', default=False)
    status = models.CharField(verbose_name='статус', max_length=16, choices=STATUS, default='у владельца')
    litter = models.ForeignKey(verbose_name='литера', to='Litter', related_name='children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    date_of_add = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)
    name = models.CharField(verbose_name='кличка', max_length=32)
    prefix = models.ForeignKey(verbose_name='приставка', to='Prefix', related_name='rats',
                               on_delete=models.SET_NULL, null=True, blank=True)
    variety = models.CharField(verbose_name='разновидность', max_length=128)
    gender = models.CharField(verbose_name='пол', max_length=8, choices=GENDER, default='самец')
    title = models.CharField(verbose_name='титул', max_length=16, choices=TITLE, default='нет')
    date_of_birth = models.DateField(verbose_name='дата рождения', default=date.today)
    date_of_death = models.DateField(verbose_name='дата смерти', default=None, null=True, blank=True)
    breeder = models.ForeignKey(verbose_name='заводчик', to='Person', related_name='rats_bred', on_delete=models.SET_NULL,
                                null=True, blank=True)
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

    def main_photo(self):
        try:
            return self.photos.all().last().picture.url
        except AttributeError:
            return None

    def status_based_on_gender(self):
        if self.gender == 'самка':
            if self.status == 'свободен':
                return 'свободна'
            elif self.status == 'зарезервирован':
                return 'зарезервирована'
        else:
            return self.status

    def full_name(self):
        string = self.name
        if self.prefix:
            if self.gender == 'самец':
                string = f'{self.name} {self.prefix.male_name}'
                if not self.prefix.suffix:
                    string = f'{self.prefix.male_name} {self.name}'
            else:
                string = f'{self.name} {self.prefix.female_name}'
                if not self.prefix.suffix:
                    string = f'{self.prefix.female_name} {self.name}'
        return string

    def lifespan(self):
        lifespan = self.date_of_death - self.date_of_birth
        seconds = lifespan.total_seconds()
        return get_timedelta_as_string(seconds)

    def current_age(self):
        lifespan = date.today() - self.date_of_birth
        seconds = lifespan.total_seconds()
        return get_timedelta_as_string(seconds)

    def __str__(self):
        return self.full_name()
