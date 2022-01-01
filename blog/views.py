from django.db.models import fields
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import BlogPost, BlogAuthor, BlogComment

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_posts = BlogPost.objects.count()
    num_authors = BlogAuthor.objects.count()
    num_comments = BlogComment.objects.count()

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_posts': num_posts,
        'num_authors': num_authors,
        'num_comments': num_comments,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor

class BlogCommentCreate(generic.edit.CreateView):
    model = BlogComment
    fields = ['description']

    def form_valid(self, form):
        """
        Add author and associated blog to form data before saving it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.author

        # Associate comment with blog post based on passed id
        form.instance.blog_post = get_object_or_404(BlogPost, pk = self.kwargs['pk'])

        # Call super-class form validation behavior
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        pass