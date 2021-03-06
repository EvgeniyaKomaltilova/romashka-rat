from django.test import TestCase


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


class ContractPageTest(TestCase):
    """Тестирование отображения страницы с договором на продажу крысенка"""

    def test_contract_returns_correct_html(self):
        """тест: используется шаблон contract"""
        response = self.client.get('/contract/')
        self.assertTemplateUsed(response, 'website/contract.html')


class VarietiesPageTest(TestCase):
    """Тестирование отображения страницы информации о разновидностях крыс"""

    def test_varieties_returns_correct_html(self):
        """тест: используется шаблон varieties"""
        response = self.client.get('/varieties/')
        self.assertTemplateUsed(response, 'website/varieties.html')


class ColorsPageTest(TestCase):
    """Тестирование отображения страницы информации об окрасах крыс"""

    def test_colors_returns_correct_html(self):
        """тест: используется шаблон colors"""
        response = self.client.get('/colors/')
        self.assertTemplateUsed(response, 'website/colors.html')


class MarkingsPageTest(TestCase):
    """Тестирование отображения страницы информации о маркировках крыс"""

    def test_markings_returns_correct_html(self):
        """тест: используется шаблон markings"""
        response = self.client.get('/markings/')
        self.assertTemplateUsed(response, 'website/markings.html')


class ArchivePageTest(TestCase):
    """Тестирование отображения страницы архива новостей"""

    def test_archive_returns_correct_html(self):
        """тест: используется шаблон archive"""
        response = self.client.get('/archive/')
        self.assertTemplateUsed(response, 'website/archive.html')
