from datetime import datetime
from django.db import models
from romashka.services.naming import get_entry_name


class Question(models.Model):
    """Модель вопроса на сайте"""

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы посетителей сайта'

    email = models.EmailField(verbose_name='Электронная почта')
    text = models.TextField(verbose_name='текст записи', max_length=512)

    def __str__(self):
        return f'Вопрос #{self.id} ({self.email})'
