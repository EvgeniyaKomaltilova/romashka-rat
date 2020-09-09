from datetime import date
from django.test import TestCase
from website.models.Image import Image
from website.models.Questionnaire import Questionnaire
from website.models.Rat import Rat
from website.models.Prefix import Prefix
from website.models.Person import Person
from website.models.Location import Location
from website.models.Litter import Litter
from website.models.Entry import Entry


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


class QuestionnaireModelTest(TestCase):
    """Тестирование модели Questionnaire"""

    def test_can_saving_and_retrieving_questionnaires(self):
        Questionnaire.objects.create(name='first')
        Questionnaire.objects.create(name='second')
        questionnaires = Questionnaire.objects.all()
        self.assertEqual(questionnaires.count(), 2)
        self.assertEqual(questionnaires[0].name, 'first')
        self.assertEqual(questionnaires[1].name, 'second')
