from django import forms
from .models import Registration, Session

DIETARY_CHOICES = [
    ('vegetarian', 'Vegetarian'),
    ('vegan', 'Vegan'),
    ('gluten_free', 'Gluten-Free'),
    ('halal', 'Halal'),
    ('kosher', 'Kosher'),
    ('nut_free', 'Nut-Free'),
]

class RegistrationForm(forms.ModelForm):
    dietary_preferences = forms.MultipleChoiceField(
        choices=DIETARY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = Registration
        fields = '__all__'
        labels = {
            "full_name": "Your Full Name:",
            "email_address": "Your Email:",
            "phone_number": "Your Phone Number:",
            "session": "Desired Session:",
            "dietary_preferences": "Dietary Preferences:"
        }