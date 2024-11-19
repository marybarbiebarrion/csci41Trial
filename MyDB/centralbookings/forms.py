# centralbookings/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Organizer, ContactPerson

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'role')

class CustomAuthenticationForm(AuthenticationForm):
    pass

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['Organizer_Name', 'Organizer_Address', 'Organizer_Type']

class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = ['Contact_Name', 'Contact_Email', 'Contact_Number']
