from django.test import TestCase
from website.models import New, Image


class IndexPageTest(TestCase):
    """Тестирование отображения домашней страницы"""

    def test_index_returns_correct_html(self):
        """тест: используется шаблон index"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'website/index.html')


class NewModelTest(TestCase):
    """Тестирование модели New"""

    def test_can_saving_and_retrieving_news(self):
        New.objects.create(text="first")
        New.objects.create(text="second")
        news = New.objects.all()
        self.assertEqual(news.count(), 2)
        self.assertEqual(news[0].text, "first")
        self.assertEqual(news[1].text, "second")


class ImageModelTest(TestCase):
    """Тестирование модели Image"""

    def test_can_saving_and_retrieving_images(self):
        Image.objects.create(name="first")
        Image.objects.create(name="second")
        news = Image.objects.all()
        self.assertEqual(news.count(), 2)
        self.assertEqual(news[0].name, "first")
        self.assertEqual(news[1].name, "second")
