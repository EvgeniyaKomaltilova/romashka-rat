from django.test import TestCase
from website.models.Image import Image
from website.models.Entry import Entry


class ImageModelTest(TestCase):
    """Тестирование модели Image"""

    def test_can_saving_and_retrieving_images(self):
        """тест: объект изображения сохраняется"""
        entry = Entry.objects.create()
        Image.objects.create(main_page=True, name='first', entry=entry)
        Image.objects.create(name='second')
        images = Image.objects.all()
        self.assertEqual(images.count(), 2)
        self.assertEqual(images[0].main_page, True)
        self.assertEqual(images[0].name, 'first')
        self.assertEqual(images[0].entry, entry)
        self.assertEqual(images[1].name, 'second')


class EntryModelTest(TestCase):
    """Тестирование модели Entry"""

    def test_can_saving_and_retrieving_entries(self):
        """тест: объект записи сохраняется"""
        Entry.objects.create(public=True, topic='test_topic', title='test_title', text='first')
        Entry.objects.create(text='second')
        entries = Entry.objects.all()
        self.assertEqual(entries.count(), 2)
        self.assertEqual(entries[0].public, True)
        self.assertEqual(entries[0].topic, 'test_topic')
        self.assertEqual(entries[0].title, 'test_title')
        self.assertEqual(entries[0].text, 'first')
        self.assertEqual(entries[1].text, 'second')
