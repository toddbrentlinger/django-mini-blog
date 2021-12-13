from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogs'),
    path('blog/<uuid:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),

]