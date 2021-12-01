# Generated by Django 3.2.9 on 2021-12-01 00:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of author of blog.', max_length=200)),
                ('bio', models.TextField(help_text='Enter biography about author of blog.', max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular blog post.', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Enter title of blog post.', max_length=200)),
                ('post_date', models.DateField(auto_now_add=True, verbose_name='Post Date')),
                ('description', models.TextField(help_text='Enter main content text of blog post.', max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogauthor')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Post Date')),
                ('author', models.CharField(help_text='Enter username of the blog comment.', max_length=200)),
                ('description', models.TextField(help_text='Enter content of blog comment.', max_length=1000)),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost', verbose_name='Blog Post')),
            ],
            options={
                'ordering': ['post_date_time'],
            },
        ),
    ]
