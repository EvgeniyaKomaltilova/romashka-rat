from datetime import date
from django.db import models
from . import Prefix, Person, Rat


class Litter(models.Model):
    public = models.BooleanField(verbose_name='опубликовать', default=True)
    name = models.CharField(verbose_name='название', max_length=8)
    prefix = models.ForeignKey(verbose_name='приставка', to='Prefix', related_name='litters',
                               on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(verbose_name='номер', max_length=16, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='дата рождения', default=date.today)
    father = models.ForeignKey(verbose_name='отец', to='Rat', related_name='father_litters', on_delete=models.SET_NULL,
                               null=True, blank=True)
    mother = models.ForeignKey(verbose_name='мать', to='Rat', related_name='mother_litters', on_delete=models.SET_NULL,
                               null=True, blank=True)
    breeder = models.ForeignKey(verbose_name='заводчик', to='Person', related_name='litters', on_delete=models.SET_NULL,
                                null=True, blank=True)

    class Meta:
        verbose_name = 'литеру'
        verbose_name_plural = 'Литеры'

    def full_name(self):
        string = self.name
        if self.prefix:
            string = f'{self.name} {self.prefix.male_name}'
            if not self.prefix.suffix:
                string = f'{self.prefix.male_name} {self.name}'

        return string

    def __str__(self):
        if self.father:
            father_name = self.father.name
        else:
            father_name = 'мать неизвестна'
        if self.mother:
            mother_name = self.mother.name
        else:
            mother_name = 'отец неизвестен'

        return f'{self.name} ({father_name} x {mother_name})'
