from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import events

RESOURCE_TYPES = (
    ('Vehicle', 'Vehicles: cars, vans, bikes'),
    ('Props', 'Props and set dressing'),
    ('Costume', 'Costumes and styling'),
    ('Animal', 'Animals and trained performers'),
    ('Equipment', 'Camera, lighting and sound equipment'),
    ('Furniture', 'Furniture and practical set items'),
    ('Catering', 'Catering and on-set services'),
    ('Crew', 'Crew, security and manpower'),
    ('Other', 'Other production requirement'),
)

class EventForm(forms.ModelForm):
    types = forms.ChoiceField(choices=RESOURCE_TYPES, label='Resource category')
    topic = forms.ChoiceField(
        choices=(
            ('Film production', 'Film production'),
            ('Short film', 'Short film'),
            ('Feature film', 'Feature film'),
            ('Advertisement', 'Advertisement'),
            ('Music video', 'Music video'),
            ('Web series', 'Web series'),
            ('Photo shoot', 'Photo shoot'),
            ('Other', 'Other'),
        ),
        label='Shoot requirement / use',
        initial='Film production',
    )
    title = forms.CharField(label='Resource or service name')
    location = forms.CharField(label='Available city / location')
    starts = forms.CharField(label='Available from', required=False)
    ends = forms.CharField(label='Available until', required=False)
    organiser = forms.CharField(label='Owner / supplier name', required=False)
    description2 = forms.CharField(label='Supplier notes', required=False)
    tickets = forms.CharField(label='Rate or booking notes', required=False)
    contact = forms.CharField(label='Contact phone', required=False)
    email = forms.EmailField(label='Contact email', required=False)

    class Meta:
        model = events
        fields = ['title', 'location', 'types', 'topic', 'starts', 'ends', 'image', 'description', 'organiser', 'description2', 'tickets', 'contact', 'email']
        widgets = {'description': CKEditor5Widget(config_name='default')}
