from django.test import TestCase

# Create your tests here.

from .models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Medu',last_name='Vada')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label=author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_length(self):
        author=Author.objects.get(id=1)
        max_length=author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_last_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_last_name_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length,100)