from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import databank

class RentalForm(forms.ModelForm):
    class Meta:
        model = databank
        fields = ['title', 'category', 'content', 'price', 'rental_period', 'availability', 'location', 'contact', 'owner', 'email', 'photo']
        widgets = {'content': CKEditor5Widget(config_name='default')}

    title = forms.CharField(label='Location name')
    category = forms.ChoiceField(choices=(
        ('House', 'House / apartment'),
        ('Office', 'Office / commercial space'),
        ('Studio', 'Studio / sound stage'),
        ('Outdoor', 'Outdoor / landscape'),
        ('Hotel', 'Hotel / hospitality space'),
        ('Warehouse', 'Warehouse / industrial'),
        ('Street', 'Street / public-facing space'),
        ('Other', 'Other shoot location'),
    ), label='Location type')
    content = forms.CharField(label='Location description', widget=CKEditor5Widget(config_name='default'))
    price = forms.CharField(label='Rate amount', help_text='Enter the amount, for example 2500.')
    rental_period = forms.ChoiceField(choices=(
        ('hourly', 'Per hour'),
        ('daily', 'Per day'),
        ('quote', 'Request a quote'),
    ), label='Pricing unit')
    availability = forms.CharField(label='Availability', required=False, help_text='Example: Weekdays, or 10-25 September.')
    location = forms.CharField(label='Address / city')
    contact = forms.CharField(label='Contact phone', required=False)
    owner = forms.CharField(label='Contact person / business', required=False)
