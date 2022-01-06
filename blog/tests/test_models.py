from django.test import TestCase
from blog.models import BlogAuthor, BlogPost, BlogComment

# Create your tests here.
class BlogAuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BlogAuthor.objects.create(name='John', bio='lorem ipsum biography.')

    # Labels

    def test_name_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_bio_label(self):
        author = BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    # Max Length

    def test_name_max_length(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_bio_max_length(self):
        author = BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEqual(max_length, 1000)

    # __str__

    def test_object_name_is_name(self):
        author = BlogAuthor.objects.get(id=1)
        expected_object_name = author.name
        self.assertEqual(str(author), expected_object_name)

    # Get Absolute URL

    def test_get_absolute_url(self):
        author = BlogAuthor.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/blog/blogger/1')

class BlogPostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BlogPost.objects.create(title='Blog Post Title', author=BlogAuthor.objects.create(name='John', bio='lorem ipsum biography...'), description='lorem ipsum blog post.')
    
    # Labels

    def test_title_label(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        field_label = blogpost._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_post_date_label(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        field_label = blogpost._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'Post Date')

    def test_author_label(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        field_label = blogpost._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_description_label(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        field_label = blogpost._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    # Max Length

    def test_title_max_length(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        max_length = blogpost._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_title_max_length(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        max_length = blogpost._meta.get_field('description').max_length
        self.assertEqual(max_length, 10000)

    # __str__

    def test_object_name_is_title_author(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        expected_object_name = f'{blogpost.title} - {blogpost.author}'
        self.assertEqual(str(blogpost), expected_object_name)

    # Get Absolute URL

    def test_get_absolute_url(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        # This will also fail if the urlconf is not defined.
        self.assertEqual(blogpost.get_absolute_url(), f'/blog/blog/{str(blogpost.id)}')

class BlogCommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        blogpost = BlogPost.objects.create(title='Blog Post Title', author=BlogAuthor.objects.create(name='John', bio='lorem ipsum biography...'), description='lorem ipsum blog post.')
        BlogComment.objects.create(blog_post=blogpost, author='User01', description='lorem ipsum comment description...')
    
    # Labels

    def test_post_date_time_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('post_date_time').verbose_name
        self.assertEqual(field_label, 'Post Date')

    def test_author_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_description_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_blog_post_label(self):
        blogcomment = BlogComment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('blog_post').verbose_name
        self.assertEqual(field_label, 'Blog Post')

    # Max Length

    def test_author_max_length(self):
        blogcomment = BlogComment.objects.get(id=1)
        max_length = blogcomment._meta.get_field('author').max_length
        self.assertEqual(max_length, 200)

    def test_description_max_length(self):
        blogcomment = BlogComment.objects.get(id=1)
        max_length = blogcomment._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    # __str__

    def test_object_name_is_author_description(self):
        blogcomment = BlogComment.objects.get(id=1)
        expected_object_name = f'{blogcomment.author} - {blogcomment.description}'
        self.assertEqual(str(blogcomment), expected_object_name)