from datetime import date
from django.db import models
from romashka.services.litters_string import get_litters_as_string
from romashka.services.photo import get_main_photo
from romashka.services.status import get_status_based_on_gender
from romashka.services.timedelta import get_rat_lifespan, get_rat_current_age
from romashka.services.naming import get_full_rat_name
from romashka.services.absolute_urls import get_rat_url


class Rat(models.Model):
    """Модель крысы"""

    class Meta:
        verbose_name = 'Крысу'
        verbose_name_plural = 'Крысы'

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

    def save(self, *args, **kwargs):
        """Изменение базовых правил сохранения крысы"""
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
        """Главное фото: последнее добавленное"""
        return get_main_photo(self)

    def status_based_on_gender(self):
        """Статус крысы с учетом окончания -а в женском роде"""
        return get_status_based_on_gender(self)

    @property
    def full_name(self):
        """Полное имя: кличка и приставка питомника"""
        return get_full_rat_name(self)

    def lifespan(self):
        """Продолжительность жизни умершей крысы"""
        return get_rat_lifespan(self)

    def current_age(self):
        """Возраст крысы на данный момент времени"""
        return get_rat_current_age(self)

    def litters(self):
        """Все пометы, рожденные крысой"""
        return get_litters_as_string(self)

    def url(self):
        """Ссылка на крысу"""
        return get_rat_url(self)

    def __str__(self):
        return self.full_name
