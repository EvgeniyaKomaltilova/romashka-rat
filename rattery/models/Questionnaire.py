from datetime import datetime
from django.db import models


class Questionnaire(models.Model):
    """Модель анкеты для потенциальных владельцев"""

    class Meta:
        verbose_name = 'Анкету'
        verbose_name_plural = 'Анкеты'

    read = models.BooleanField(verbose_name='прочитано', default=False)
    approved = models.BooleanField(verbose_name='одобрено', default=False)
    date = models.DateTimeField(verbose_name='дата заполнения', default=datetime.now)
    name = models.CharField(verbose_name='ФИО', max_length=64, null=True)
    contact = models.CharField(verbose_name='контакты', max_length=64, null=True)
    age = models.PositiveIntegerField(verbose_name='возраст', null=True)
    location = models.CharField(verbose_name='место проживания', max_length=64, null=True)
    which_baby_rat = models.CharField(verbose_name='Какой крысенок интересует', max_length=128, null=True)
    allergy = models.TextField(verbose_name='Наличие аллергии', max_length=256, null=True)
    know_how = models.TextField(verbose_name='Осведомленность в вопросах содержания', max_length=512, null=True)
    pet_or_breed = models.TextField(verbose_name='Любимец или в разведение', max_length=256, null=True)
    friend = models.TextField(verbose_name='Наличие друга для крысенка', max_length=512, null=True)
    contract = models.TextField(verbose_name='Готовность подписать договор', max_length=64, null=True)
    recommendation = models.TextField(verbose_name='Наличие рекомендаций', max_length=256, null=True)
    additionally = models.TextField(verbose_name='Дополнительно', max_length=4096, null=True)

    def __str__(self):
        return self.name
