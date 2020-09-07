from django.test import TestCase
from website.models import Rat, Litter


class IndexPageTest(TestCase):
    """Тестирование отображения домашней страницы"""

    def test_index_returns_correct_html(self):
        """тест: используется шаблон index"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'website/index.html')


class AboutPageTest(TestCase):
    """Тестирование отображения страницы информации о питомнике"""

    def test_archive_returns_correct_html(self):
        """тест: используется шаблон about"""
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'website/about.html')


class ArchivePageTest(TestCase):
    """Тестирование отображения страницы архива новостей"""

    def test_archive_returns_correct_html(self):
        """тест: используется шаблон archive"""
        response = self.client.get('/archive/')
        self.assertTemplateUsed(response, 'website/archive.html')


class RatsPageTest(TestCase):
    """Тестирование отображения списка крыс"""

    def test_rats_returns_correct_html(self):
        """тест: используется шаблон rats"""
        response = self.client.get('/rats/')
        self.assertTemplateUsed(response, 'website/rats.html')


class RatPageTest(TestCase):
    """Тестирование отображения страницы конкретной крысы"""

    def test_rat_returns_correct_html(self):
        """тест: используется шаблон rat"""
        Rat.objects.create()
        response = self.client.get('/rats/1/')
        self.assertTemplateUsed(response, 'website/rat.html')


class LittersPageTest(TestCase):
    """Тестирование отображения списка литер"""

    def test_litters_returns_correct_html(self):
        """тест: используется шаблон litters"""
        response = self.client.get('/litters/')
        self.assertTemplateUsed(response, 'website/litters.html')


class LitterPageTest(TestCase):
    """Тестирование отображения страницы конкретной литеры"""

    def test_litter_returns_correct_html(self):
        """тест: используется шаблон litter"""
        Litter.objects.create()
        response = self.client.get('/litters/1/')
        self.assertTemplateUsed(response, 'website/litter.html')
