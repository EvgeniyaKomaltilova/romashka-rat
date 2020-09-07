from datetime import date
from django.test import TestCase
from website.models import Image, Rat, Prefix, Person, Location, Litter, Entry


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

    def test_lifespan_returns_right_time_string(self):
        Rat.objects.create(name='first', date_of_birth=date(2015, 9, 1), date_of_death=date(2015, 10, 15))
        rat = Rat.objects.first()
        self.assertEqual(rat.lifespan(), '1 месяц')

    def test_current_age_returns_right_time_string(self):
        pass


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


class EntryModelTest(TestCase):
    """Тестирование модели Entry"""

    def test_can_saving_and_retrieving_entries(self):
        Entry.objects.create(text='first')
        Entry.objects.create(text='second')
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 2)
        self.assertEqual(entries[0].text, 'first')
        self.assertEqual(entries[1].text, 'second')