from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BlogPost, BlogComment, BlogAuthor

# Register your models here.
admin.site.register(User, UserAdmin)
# admin.site.register(BlogPost)
# admin.site.register(BlogComment)
# admin.site.register(BlogAuthor)

class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 0

class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 0

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'id')
    list_filter = ('post_date',)
    inlines = [BlogCommentInline]

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'author', 'post_date_time')
    list_filter = ('post_date_time',)

@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    inlines = [BlogPostInline]