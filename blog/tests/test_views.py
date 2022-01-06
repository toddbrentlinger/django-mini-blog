from django.test import TestCase
from django.urls import reverse

from blog.models import User, BlogAuthor, BlogPost, BlogComment

# Create your tests here.

class BlogAuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 8 authors for pagination tests
        number_of_authors = 8

        for author_id in range(number_of_authors):
            BlogAuthor.objects.create(
                name=f'Name {author_id}',
                bio=f'Biography {author_id}...'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogauthor_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blogauthor_list']), 5)

    def test_lists_all_blogauthors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('bloggers')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blogauthor_list']), 3)

class BlogCommentCreateViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        # Create blog post
        BlogPost.objects.create(
            title='Blog Post Title',
            author=BlogAuthor.objects.create(name='Blog Author Name', bio='Blog author biography...'),
            description='Blog post description...'
        )

    def test_redirect_if_not_logged_in(self):
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        response = self.client.get(reverse('blogcomment-create', kwargs={'pk': blogpost.pk}))
        self.assertRedirects(response, f'/accounts/login/?next=/blog/blog/{blogpost.id}/create-comment/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        response = self.client.get(reverse('blogcomment-create', kwargs={'pk': blogpost.pk}))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'blog/blogcomment_form.html')