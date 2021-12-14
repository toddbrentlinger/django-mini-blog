import uuid # Used for unique blog post instances

from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class BlogAuthor(models.Model):
    """Model representing a blog post author."""

    name = models.CharField(max_length=200, help_text='Enter name of author of blog.')
    bio = models.TextField(max_length=1000, help_text='Enter biography about author of blog.')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of BlogAuthor."""
        # return reverse('blog-author-detail-view', args=[str(self.id)])
        pass

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class BlogPost(models.Model):
    """Model representing a blog post."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular blog post.')
    title = models.CharField(max_length=200, help_text='Enter title of blog post.')
    post_date = models.DateField(auto_now_add=True, verbose_name='Post Date')
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    description = models.TextField(max_length=10000, help_text='Enter main content text of blog post.')

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of BlogPost."""
        return reverse('blogpost-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} - {self.author} - {self.id}'

class BlogComment(models.Model):
    """Model representing a comment"""

    post_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Post Date')
    author = models.CharField(max_length=200, help_text='Enter username of the blog comment.')
    description = models.TextField(max_length=1000, help_text='Enter content of blog comment.')
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name='Blog Post')

    class Meta:
        ordering = ['post_date_time']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.author} - {self.description}'