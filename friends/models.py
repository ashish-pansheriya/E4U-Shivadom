from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from application.models import databank
from django_ckeditor_5.fields import CKEditor5Field

FILM_ROLE_CHOICES = (
    ('Actor', 'Actor / Actress'), ('Child Artist', 'Child Artist'), ('Model', 'Model'),
    ('Dancer', 'Dancer'), ('Singer', 'Singer / Musician'), ('Choreographer', 'Choreographer'),
    ('Writer', 'Writer / Lyricist'), ('Director', 'Creative Director'),
    ('Casting', 'Casting Director / Agency'),
    ('Cinematographer', 'Cinematographer / Camera Operator'), ('Editor', 'Editor / VFX Artist'),
    ('Photographer', 'Photographer'), ('Makeup', 'Makeup Artist / Hair Stylist'),
    ('Costume', 'Costume Designer / Stylist'), ('Art Department', 'Art Director / Set Designer'),
    ('Sound', 'Sound Engineer'), ('Lighting', 'Lighting Technician'),
    ('Production', 'Production Manager'), ('Crew', 'Crew / Manpower'),
    ('Vendor', 'Equipment or Location Vendor'), ('Audience', 'Audience / Film Enthusiast'),
)

CITY_CHOICES = (
    ('Mumbai', 'Mumbai'), ('Navi Mumbai', 'Navi Mumbai'), ('Pune', 'Pune'), ('Ahmedabad', 'Ahmedabad'),
    ('Vadodara', 'Vadodara'), ('Surat', 'Surat'), ('Delhi', 'Delhi NCR'), ('Chandigarh', 'Chandigarh'),
    ('Jaipur', 'Jaipur'), ('Kolkata', 'Kolkata'), ('Bengaluru', 'Bengaluru'), ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'), ('Kochi', 'Kochi'), ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Lucknow', 'Lucknow'), ('Bhopal', 'Bhopal'), ('Indore', 'Indore'), ('Goa', 'Goa'),
    ('Other India', 'Other India'), ('International', 'Outside India'),
)

EYE_COLOR_CHOICES = (
    ('Black', 'Black'), ('Brown', 'Brown'), ('Hazel', 'Hazel'), ('Blue', 'Blue'), ('Green', 'Green'), ('Gray', 'Gray'),
    ('Not specified', 'Not specified'),
)

HAIR_COLOR_CHOICES = (
    ('Black', 'Black'), ('Brown', 'Brown'), ('Blonde', 'Blonde'), ('Dark Brown', 'Dark Brown'), ('Red', 'Red'),
    ('Gray', 'Gray'), ('Not specified', 'Not specified'),
)


class friends(models.Model):

    ages = (
        ('Choose one', 'Choose one'),
        ('till-20', 'till-20'),
        ('20-24', '20-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55-64', '55-64'),
        ('65 or older', '65 or older'),
        ('I prefer to keep secret', 'I prefer to keep secret'),
    )


    type = (
        ('Choose one', 'Choose one'),
        ('Athletic/Muscular', 'Athletic/Muscular'),
        ('Slim/Slender', 'Slim/Slender'),
        ('Average', 'Average'),
        ('A little above average', 'A little above average'),
        ('Full Figured', 'Full Figured'),
    )
    heights = (
        ('Choose one', 'Choose one'),
        ('Very Short', 'Very Short'),
        ('Short', 'Short'),
        ('Average', 'Average'),
        ('Above Average', 'Above Average'),
        ('Tall', 'Tall'),
    )
    fee = (
        ('negotiable', 'negotiable'),
        ('₹50 / day', '₹50 / day'), ('₹100 / day', '₹100 / day'), ('₹200 / day', '₹200 / day'),
        ('₹500 / day', '₹500 / day'), ('₹1,000 / day', '₹1,000 / day'), ('₹2,000 / day', '₹2,000 / day'),
        ('₹3,000 / day', '₹3,000 / day'), ('₹4,000 / day', '₹4,000 / day'), ('₹5,000 / day', '₹5,000 / day'),
    )
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=100, null=True, verbose_name='Nickname')
    age = models.CharField(max_length=100, null=True, default='Choose one', choices=ages, verbose_name='What is your age?')
    activities = models.CharField(max_length=200, null=True, default='I am up for ', verbose_name='E4U take 25% on Pay')
    gender = models.CharField(max_length=20, null=True, choices=gender_choices, verbose_name='Gender')
    body = models.CharField(max_length=200, null=True, choices=type, default='Choose one', verbose_name='Body Type')
    height = models.CharField(max_length=50, null=True, choices= heights, default='Choose one', verbose_name='Height')
    eye_color = models.CharField(max_length=25, choices=EYE_COLOR_CHOICES, default='Not specified', blank=True, null=True, verbose_name='Eye color')
    hair_color = models.CharField(max_length=25, choices=HAIR_COLOR_CHOICES, default='Not specified', blank=True, null=True, verbose_name='Hair color')
    weight = models.CharField(max_length=20, blank=True, null=True, verbose_name='Weight')
    bust = models.CharField(max_length=20, blank=True, null=True, verbose_name='Bust')
    waist = models.CharField(max_length=20, blank=True, null=True, verbose_name='Waist')
    hips = models.CharField(max_length=20, blank=True, null=True, verbose_name='Hips')
    shoe_size = models.CharField(max_length=20, blank=True, null=True, verbose_name='Shoe size')
    experience = models.CharField(max_length=50, blank=True, null=True, verbose_name='Experience / Years in industry')
    about = CKEditor5Field()
    language = models.CharField(max_length=100, default='English, ', null=True,verbose_name='Languages | Speak')
    address = models.CharField(max_length=100, null=True, verbose_name='Your Location')
    fees = models.CharField(max_length=50, choices=fee, default='negotiable', null=True, verbose_name='My fees')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.IntegerField(null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email id')
    photo = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Profile Picture,')
    roles = models.JSONField(default=list, blank=True, verbose_name='I am here as')
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default='Mumbai', verbose_name='Primary film city')
    showreel_url = models.URLField(blank=True, verbose_name='YouTube showreel or portfolio link')
    availability = models.CharField(max_length=100, blank=True, verbose_name='Availability')
    profile_visibility = models.CharField(max_length=10, choices=(('public', 'Public'), ('private', 'Private')), default='public')


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('friend-post-detail', kwargs={'pk': self.pk})


class frienddata(forms.ModelForm):

    class Meta:
        model = friends
        fields = ['name', 'age', 'activities', 'gender', 'body', 'height', 'fees', 'language','contact', 'email', 'address', 'about', 'photo']




class Images(models.Model):
    post = models.ForeignKey(friends, default=None, null=True, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media', null=True, verbose_name='Profile Picture,')

    def __str__(self):
        return str(self.file)


class friend(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['file']
