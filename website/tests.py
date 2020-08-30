from django.test import TestCase
from website.models import New


class IndexPageTest(TestCase):
    """Тестирование отображения домашней страницы"""

    def test_index_returns_correct_html(self):
        """тест: используется шаблон index"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'website/index.html')


class NewModelTest(TestCase):
    """Тестирование модели New"""

    def test_can_saving_and_retrieving_news(self):
        New.objects.create(text="first_new")
        New.objects.create(text="second_new")
        news = New.objects.all()
        self.assertEqual(news.count(), 2)
        self.assertEqual(news[0].text, "first_new")
        self.assertEqual(news[1].text, "second_new")
