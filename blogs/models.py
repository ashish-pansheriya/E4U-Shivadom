from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from urllib.parse import parse_qs, urlparse

class blogbank(models.Model):

    categories = (
        ('Spiritual Blog', 'Spiritual Blog'),
        ('Dating Blog', 'Dating Blog'),
        ('Love Blog', 'Love Blog'),
        ('Friends Blog', 'Friends Blog'),
        ('Fashion Blog', 'Fashion Blog'),
        ('Food Blog', 'Food Blog'),
        ('Travel Blog', 'Travel Blog'),
        ('Music Blog', 'Music Blog'),
        ('Lifestyle Blog', 'Lifestyle Blog'),
        ('Fitness Blog', 'Fitness Blog'),
        ('DIY Blog', 'DIY Blog'),
        ('Sports Blog', 'Sports Blog'),
        ('Finance Blog', 'Finance Blog'),
        ('Political Blog', 'Political Blog'),
        ('Parenting Blog', 'Parenting Blog'),
        ('Business Blog', 'Business Blog'),
        ('Personal Blog', 'Personal Blog'),
        ('Movie Blog', 'Movie Blog'),
        ('Car Blog', 'Car Blog'),
        ('News Blog', 'News Blog'),
        ('Pet Blog', 'Pet Blog'),
        ('Gaming Blog', 'Gaming Blog'),
        ('Technology Blog', 'Technology Blog'),
        ('Religious Blog', 'Religious Blog'),
        ('Story Blog', 'Story Blog'),
        ('Blog', 'Blog')
    )
    title = models.CharField(max_length=300, verbose_name='Blog Title')
    category = models.CharField(max_length=20, null=True, choices=categories, default='Blog', verbose_name='Blog About')
    content = CKEditor5Field()
    photo = models.ImageField(upload_to='media', verbose_name='Blog Image')
    name = models.CharField( max_length=50,  null=True, verbose_name='Creator Name')
    email = models.EmailField(max_length=50, null=True, verbose_name='Creator Email')
    location = models.CharField(max_length=100, null=True, verbose_name='Location')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Owner')
    youtube_url = models.URLField(blank=True, verbose_name='YouTube video link')

    @property
    def youtube_embed_url(self):
        if not self.youtube_url:
            return ''
        parsed = urlparse(self.youtube_url)
        hostname = parsed.netloc.lower()
        if hostname.endswith('youtu.be'):
            video_id = parsed.path.strip('/').split('/')[0]
        elif hostname.endswith('youtube.com'):
            video_id = parse_qs(parsed.query).get('v', [''])[0]
            if not video_id and parsed.path.startswith('/shorts/'):
                video_id = parsed.path.split('/shorts/', 1)[1].split('/', 1)[0]
            if not video_id and parsed.path.startswith('/embed/'):
                video_id = parsed.path.split('/embed/', 1)[1].split('/', 1)[0]
        else:
            video_id = ''
        return f'https://www.youtube.com/embed/{video_id}?rel=0' if video_id else ''

    @property
    def youtube_thumbnail_url(self):
        embed_url = self.youtube_embed_url
        if not embed_url:
            return ''
        video_id = embed_url.split('/embed/', 1)[1].split('?', 1)[0]
        return f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


class BlogImage(models.Model):
    blog = models.ForeignKey(blogbank, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='blog_gallery')
    caption = models.CharField(max_length=160, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

