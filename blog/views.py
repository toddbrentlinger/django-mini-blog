from django.shortcuts import render
from django.views import generic
from .models import BlogPost, BlogAuthor, BlogComment

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_posts = BlogPost.objects.count()
    num_authors = BlogAuthor.objects.count()
    num_comments = BlogComment.objects.count()

    context = {
        'num_posts': num_posts,
        'num_authors': num_authors,
        'num_comments': num_comments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

class BlogPostListView(generic.ListView):
    model = BlogPost

class BlogPostDetailView(generic.DetailView):
    model = BlogPost