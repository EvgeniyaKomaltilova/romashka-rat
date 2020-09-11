from django.test import TestCase

from rattery.models.Litter import Litter
from rattery.models.Rat import Rat


class QuestionnaireFormPageTest(TestCase):
    """Тестирование отображения формы"""

    def test_questionnaire_returns_correct_html(self):
        """тест: используется шаблон questionnaire"""
        response = self.client.get('/rats/questionnaire/')
        self.assertTemplateUsed(response, 'rattery/questionnaire.html')


class QuestionnaireSuccessPageTest(TestCase):
    """Тестирование отображения страницы успешного заполнения формы"""

    def test_questionnaire_success_returns_correct_html(self):
        """тест: используется шаблон success"""
        response = self.client.get('/rats/questionnaire/success/')
        self.assertTemplateUsed(response, 'rattery/questionnaire_success.html')


class MaleRatsPageTest(TestCase):
    """Тестирование отображения списка крыс-самцов"""

    def test_male_rats_returns_correct_html(self):
        """тест: используется шаблон male_rats"""
        response = self.client.get('/rats/male/')
        self.assertTemplateUsed(response, 'rattery/male_rats.html')


class FemaleRatsPageTest(TestCase):
    """Тестирование отображения списка крыс-самок"""

    def test_female_rats_returns_correct_html(self):
        """тест: используется шаблон female_rats"""
        response = self.client.get('/rats/female/')
        self.assertTemplateUsed(response, 'rattery/female_rats.html')


class RatPageTest(TestCase):
    """Тестирование отображения страницы конкретной крысы"""

    def test_rat_returns_correct_html(self):
        """тест: используется шаблон rat"""
        Rat.objects.create()
        response = self.client.get('/rats/1/')
        self.assertTemplateUsed(response, 'rattery/rat.html')


class LittersPageTest(TestCase):
    """Тестирование отображения списка литер"""

    def test_litters_returns_correct_html(self):
        """тест: используется шаблон litters"""
        response = self.client.get('/rats/litters/2020/')
        self.assertTemplateUsed(response, 'rattery/litters.html')


class LitterPageTest(TestCase):
    """Тестирование отображения страницы конкретной литеры"""

    def test_litter_returns_correct_html(self):
        """тест: используется шаблон litter"""
        Litter.objects.create(year=2020)
        response = self.client.get('/rats/litters/2020/1/')
        self.assertTemplateUsed(response, 'rattery/litter.html')
