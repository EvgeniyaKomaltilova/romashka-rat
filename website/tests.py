from django.test import TestCase
from website.models import New, Image, Rat, Prefix, Person, Location, Litter


class IndexPageTest(TestCase):
    """Тестирование отображения домашней страницы"""

    def test_index_returns_correct_html(self):
        """тест: используется шаблон index"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'website/index.html')


class ArchivePageTest(TestCase):
    """Тестирование отображения страницы архива новостей"""

    def test_index_returns_correct_html(self):
        """тест: используется шаблон archive"""
        response = self.client.get('/archive/')
        self.assertTemplateUsed(response, 'website/archive.html')


class NewModelTest(TestCase):
    """Тестирование модели New"""

    def test_can_saving_and_retrieving_news(self):
        New.objects.create(text='first')
        New.objects.create(text='second')
        news = New.objects.all()
        self.assertEqual(news.count(), 2)
        self.assertEqual(news[0].text, 'first')
        self.assertEqual(news[1].text, 'second')


class ImageModelTest(TestCase):
    """Тестирование модели Image"""

    def test_can_saving_and_retrieving_images(self):
        Image.objects.create(name='first')
        Image.objects.create(name='second')
        images = Image.objects.all()
        self.assertEqual(images.count(), 2)
        self.assertEqual(images[0].name, 'first')
        self.assertEqual(images[1].name, 'second')


class RatModelTest(TestCase):
    """Тестирование модели Rat"""

    def test_can_saving_and_retrieving_rats(self):
        Rat.objects.create(name='first')
        Rat.objects.create(name='second')
        rats = Rat.objects.all()
        self.assertEqual(rats.count(), 2)
        self.assertEqual(rats[0].name, 'first')
        self.assertEqual(rats[1].name, 'second')


class PrefixModelTest(TestCase):
    """Тестирование модели Prefix"""

    def test_can_saving_and_retrieving_prefix(self):
        Prefix.objects.create(male_name='first')
        Prefix.objects.create(male_name='second')
        prefixes = Prefix.objects.all()
        self.assertEqual(prefixes.count(), 2)
        self.assertEqual(prefixes[0].male_name, 'first')
        self.assertEqual(prefixes[1].male_name, 'second')


class PersonModelTest(TestCase):
    """Тестирование модели Person"""

    def test_can_saving_and_retrieving_person(self):
        Person.objects.create(first_name='first')
        Person.objects.create(first_name='second')
        persons = Person.objects.all()
        self.assertEqual(persons.count(), 2)
        self.assertEqual(persons[0].first_name, 'first')
        self.assertEqual(persons[1].first_name, 'second')


class LocationModelTest(TestCase):
    """Тестирование модели Location"""

    def test_can_saving_and_retrieving_locations(self):
        Location.objects.create(city='first')
        Location.objects.create(city='second')
        locations = Location.objects.all()
        self.assertEqual(locations.count(), 2)
        self.assertEqual(locations[0].city, 'first')
        self.assertEqual(locations[1].city, 'second')


class LitterModelTest(TestCase):
    """Тестирование модели Litter"""

    def test_can_saving_and_retrieving_litters(self):
        Litter.objects.create(name='first')
        Litter.objects.create(name='second')
        litters = Litter.objects.all()
        self.assertEqual(litters.count(), 2)
        self.assertEqual(litters[0].name, 'first')
        self.assertEqual(litters[1].name, 'second')
