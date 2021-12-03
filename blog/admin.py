from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BlogPost, BlogComment, BlogAuthor

# Register your models here.
admin.site.register(User, UserAdmin)
# admin.site.register(BlogPost)
# admin.site.register(BlogComment)
# admin.site.register(BlogAuthor)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    pass