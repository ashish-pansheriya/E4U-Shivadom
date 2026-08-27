from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import blogbank

class BlogForm(forms.ModelForm):
    class Meta:
        model = blogbank
        fields = ['title', 'category', 'content', 'photo', 'youtube_url', 'name', 'location', 'email']
        widgets = {'content': CKEditor5Widget(config_name='default')}
