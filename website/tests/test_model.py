from django.test import TestCase
from website.models.Image import Image
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


class EntryModelTest(TestCase):
    """Тестирование модели Entry"""

    def test_can_saving_and_retrieving_entries(self):
        Entry.objects.create(text='first')
        Entry.objects.create(text='second')
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 2)
        self.assertEqual(entries[0].text, 'first')
        self.assertEqual(entries[1].text, 'second')
