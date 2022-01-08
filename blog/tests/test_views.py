import uuid

from django.test import TestCase
from django.urls import reverse

from blog.models import User, BlogAuthor, BlogPost, BlogComment

# Create your tests here.

class BlogPostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 8 posts for pagination tests
        number_of_posts = 8

        for post_id in range(number_of_posts):
            BlogPost.objects.create(
                title=f'Blog Post Title {post_id}',
                author=BlogAuthor.objects.create(name=f'Blog Author Name {post_id}', bio=f'Blog author {post_id} biography...'),
                description=f'Blog post {post_id} description...'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blogpost_list']), 5)

    def test_lists_all_blogposts(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('blogs')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blogpost_list']), 3)

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

    def test_HTTP404_for_invalid_blog_post_if_logged_in(self):
        # unlikely UID to match our bookinstance!
        test_uid = uuid.uuid4()
        login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('blogcomment-create', kwargs={'pk' : test_uid}))
        self.assertEqual(response.status_code, 404)

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

    def test_redirects_to_correct_blog_post_on_success(self):
        login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        response = self.client.post(reverse('blogcomment-create', kwargs={'pk' : blogpost.pk,}), {'description' : 'Lorem ipsum comment description...'})
        self.assertRedirects(response, reverse('blogpost-detail', kwargs={'pk' : blogpost.pk}))

    def test_correct_blog_post_property_passed_to_context(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        response = self.client.get(reverse('blogcomment-create', kwargs={'pk': blogpost.pk}))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check if 'blogpost' in context variable
        self.assertTrue('blogpost' in response.context)

    def test_correct_blog_post_value_passed_to_context(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        blogpost = BlogPost.objects.get(title='Blog Post Title')
        response = self.client.get(reverse('blogcomment-create', kwargs={'pk': blogpost.pk}))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check if same blogpost past to context variable
        self.assertTrue(response.context['blogpost'] == blogpost)