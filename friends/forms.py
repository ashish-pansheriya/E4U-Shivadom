from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import FILM_ROLE_CHOICES, friends

class TalentProfileForm(forms.ModelForm):
    roles = forms.MultipleChoiceField(
        choices=FILM_ROLE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='I am here as',
        help_text='Select every role that describes your film-industry profile.',
    )
    photo = forms.ImageField(
        required=False,
        label='Profile picture',
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*'})
    )

    class Meta:
        model = friends
        fields = [
            'name', 'roles', 'gender', 'age', 'city', 'address', 'language',
            'activities', 'about', 'availability', 'fees', 'showreel_url',
            'contact', 'email', 'photo', 'eye_color', 'hair_color', 'height', 'weight',
            'bust', 'waist', 'hips', 'shoe_size', 'experience'
        ]
        widgets = {'about': CKEditor5Widget(config_name='default')}
