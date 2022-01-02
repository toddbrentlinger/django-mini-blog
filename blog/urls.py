from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogs'),
    path('blog/<uuid:pk>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('blog/<uuid:pk>/create-comment/', views.BlogCommentCreate.as_view(), name='blogcomment-create'),
    path('bloggers/', views.BlogAuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>/', views.BlogAuthorDetailView.as_view(), name='blogauthor-detail'),
]