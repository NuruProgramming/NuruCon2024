from django import forms
from .models import Speaker, Registration, Sponsor

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'email', 'number', 'title', 'description', 'image']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone']

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['name', 'email', 'number', 'logo', 'website', 'description', 'package']
