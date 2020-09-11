from datetime import date
from django.test import TestCase

from rattery.models.Litter import Litter
from rattery.models.Location import Location
from rattery.models.Person import Person
from rattery.models.Photo import Photo
from rattery.models.Prefix import Prefix
from rattery.models.Questionnaire import Questionnaire
from rattery.models.Rat import Rat


class PhotoModelTest(TestCase):
    """Тестирование модели Photo"""

    def test_can_saving_and_retrieving_images(self):
        Photo.objects.create(name='first')
        Photo.objects.create(name='second')
        photos = Photo.objects.all()
        self.assertEqual(photos.count(), 2)
        self.assertEqual(photos[0].name, 'first')
        self.assertEqual(photos[1].name, 'second')


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


class QuestionnaireModelTest(TestCase):
    """Тестирование модели Questionnaire"""

    def test_can_saving_and_retrieving_questionnaires(self):
        Questionnaire.objects.create(name='first')
        Questionnaire.objects.create(name='second')
        questionnaires = Questionnaire.objects.all()
        self.assertEqual(questionnaires.count(), 2)
        self.assertEqual(questionnaires[0].name, 'first')
        self.assertEqual(questionnaires[1].name, 'second')
