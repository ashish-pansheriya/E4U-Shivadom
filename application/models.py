from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class databank(models.Model):

    categories = (
        ('House', 'House / apartment'), ('Office', 'Office / commercial space'),
        ('Outdoor', 'Outdoor / landscape'), ('Hotel', 'Hotel / hospitality space'),
        ('Warehouse', 'Warehouse / industrial'), ('Street', 'Street / public-facing space'),
        ('Camera & Lenses', 'Camera & Lenses'), ('Lighting', 'Lighting & Grip'),
        ('Sound', 'Sound & Recording'), ('Studio', 'Studio / Green Screen'),
        ('Location', 'Shooting Location: house, shop or office'), ('Vehicle', 'Cars, vans & transport'),
        ('Costume', 'Costumes & Styling'), ('Props', 'Props & Set Dressing'),
        ('Editing', 'Editing & VFX Equipment'), ('Crew', 'Crew, Security & Manpower'),
        ('Catering', 'Catering & Production Services'), ('Other', 'Other Film Service'),
    )
    title = models.CharField(max_length=100, verbose_name='Ad title')
    category = models.CharField(max_length=20, null=True, choices=categories, default='Other', verbose_name='Rental category')
    content = CKEditor5Field()
    price = models.CharField( max_length=50,  null=True, verbose_name='Rental rate / quote')
    location = models.CharField(max_length=100, null=True, verbose_name='Location')
    contact = models.IntegerField( null=True, verbose_name='Phone Number (Your phone number will show up on your Ad.)')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email (Your email address will not be shared with others.)')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    owner = models.CharField(max_length=17, null=True, verbose_name="Name of the owner")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Owner')
    photo = models.ImageField(upload_to='media', verbose_name='Photo')
    rental_period = models.CharField(max_length=20, choices=(('hourly', 'Hourly'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('quote', 'Request a quote')), default='daily')
    availability = models.CharField(max_length=100, blank=True, verbose_name='Availability')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
