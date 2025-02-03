from django import forms
from .models import Registration
from django.core.exceptions import ValidationError

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
        label= "Dietary Preferences (If Applicable)"
    )
    class Meta:
        model = Registration
        fields = '__all__'
        labels = {
            "full_name": "Your Full Name:",
            "email_address": "Your Email:",
            "phone_number": "Your Phone Number:",
            "session": "Desired Session:"
        }

    def clean_email_address(self):
        email = self.cleaned_data.get('email_address')
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            if Registration.objects.filter(email_address=email).exclude(pk=instance.pk).exists():
                raise ValidationError("This email address is already registered.")
        elif Registration.objects.filter(email_address=email).exists():
            raise ValidationError("This email address is already registered.")

        return email
