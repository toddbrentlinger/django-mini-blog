from django.test import TestCase
from blog.models import BlogAuthor

# Create your tests here.
class BlogAuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BlogAuthor.objects.create(name='John', bio='lorem ipsum biography.')

    def test_name_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_bio_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_name_max_length(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_bio_max_length(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_name(self):
        author = BlogAuthor.objects.get(id=1)
        expected_object_name = author.name
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = BlogAuthor.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/blog/blogger/1')
