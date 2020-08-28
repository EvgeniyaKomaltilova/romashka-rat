from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):
    """тест посетителя сайта"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def test_ability_to_navigate_the_site(self):
        """тест: перемещаемся по страницам"""
        # главная страница
        self.browser.get(self.live_server_url)
        # title корректный
        assert 'Ромашка' in self.browser.title
        # проверка заголовка
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Ромашка', header_text)
        # меню -> главная
        # главная -> свободные крысята
        # меню -> информация
        # меню -> крысы
        # крысы -> самцы
        # самцы -> самки
        # самки -> самцы
        # самцы -> страница крысы
        # меню -> крысята
        # крысята -> страница литеры
