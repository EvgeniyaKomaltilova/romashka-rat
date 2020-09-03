from datetime import datetime, date
from django.db import models


class Image(models.Model):
    date = models.DateTimeField(verbose_name='дата публикации', default=datetime.now)
    name = models.CharField(verbose_name='название', max_length=128)
    rat = models.ForeignKey(verbose_name='крыса', to='Rat', related_name='photos', on_delete=models.CASCADE,
                            null=True, blank=True)
    picture = models.ImageField(verbose_name='фото', upload_to='images')

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.name


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

    public = models.BooleanField(verbose_name='опубликовать', default=False)
    status = models.CharField(verbose_name='статус', max_length=14, choices=STATUS, default='у владельца')
    litter = models.ForeignKey(verbose_name='литера', to='Litter', related_name='babies', on_delete=models.SET_NULL,
                               null=True, blank=True)
    date_of_add = models.DateTimeField(verbose_name='дата добавления', auto_now_add=True)
    name = models.CharField(verbose_name='кличка', max_length=32)
    prefix = models.ForeignKey(verbose_name='приставка', to='Prefix', related_name='rats',
                               on_delete=models.SET_NULL, null=True, blank=True)
    variety = models.CharField(verbose_name='разновидность', max_length=128)
    gender = models.CharField(verbose_name='пол', max_length=5, choices=GENDER, default='самец')
    title = models.CharField(verbose_name='титул', max_length=12, choices=TITLE, default='нет')
    date_of_birth = models.DateField(verbose_name='дата рождения', default=date.today)
    date_of_death = models.DateField(verbose_name='дата смерти', default=None, null=True, blank=True)
    breeder = models.ForeignKey(verbose_name='заводчик', to='Person', related_name='rats_bred', on_delete=models.SET_NULL,
                                null=True, blank=True)
    owner = models.ForeignKey(verbose_name='владелец', to='Person', related_name='rats_own', on_delete=models.SET_NULL,
                              null=True, blank=True)
    father = models.ForeignKey(verbose_name='отец', to='self', related_name='fathers_children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    mother = models.ForeignKey(verbose_name='мать', to='self', related_name='mothers_children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    information = models.TextField(verbose_name='информация', max_length=2048)

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

    def __str__(self):
        string = self.name
        if self.prefix:
            if self.gender == 'самец':
                string = f'{self.name} {self.prefix.male_name}'
                if not self.prefix.suffix:
                    string = f'{self.prefix.male_name} {self.name}'
            else:
                string = f'{self.name} {self.prefix.male_name}'
                if not self.prefix.suffix:
                    string = f'{self.prefix.male_name} {self.name}'
        return string


class Prefix(models.Model):
    female_name = models.CharField(verbose_name='приставка для самки', max_length=32)
    male_name = models.CharField(verbose_name='приставка для самца', max_length=32)
    suffix = models.BooleanField(verbose_name='после клички', default=True)

    class Meta:
        verbose_name = 'приставку'
        verbose_name_plural = 'Приставки питомников'

    def __str__(self):
        return f'{self.male_name}/{self.female_name}'


class Person(models.Model):
    first_name = models.CharField(verbose_name='имя', max_length=32)
    second_name = models.CharField(verbose_name='отчество', max_length=32, null=True, blank=True)
    last_name = models.CharField(verbose_name='фамилия', max_length=32)
    location = models.ForeignKey(verbose_name='место проживания', to='Location', related_name='persons',
                                 on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'личность'
        verbose_name_plural = 'Заводчики и владельцы'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Location(models.Model):
    country = models.CharField(verbose_name='страна', max_length=32)
    city = models.CharField(verbose_name='город', max_length=32)

    class Meta:
        verbose_name = 'локацию'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'{self.city}, {self.country}'


class Litter(models.Model):
    name = models.CharField(verbose_name='название', max_length=8)
    prefix = models.ForeignKey(verbose_name='приставка', to='Prefix', related_name='litters',
                               on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(verbose_name='номер', max_length=16)
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

    def __str__(self):
        return self.name


class Entry(models.Model):

    TOPICS = [
        ('news', 'новости'),
        ('about', 'о питомнике'),
        ('varieties', 'разновидности')
    ]

    public = models.BooleanField(verbose_name='опубликовать', default=False)
    date = models.DateTimeField(verbose_name='дата добавления', default=datetime.now)
    topic = models.CharField(verbose_name='назначение', max_length=16, choices=TOPICS, null=True)
    text = models.TextField(verbose_name='текст записи', max_length=2048)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Новости и контент'

    def __str__(self):
        return self.text[:50]
