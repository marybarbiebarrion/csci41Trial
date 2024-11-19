# centralbookings/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Organizer, ContactPerson, Participant

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

#        fields = ('username', 'email', 'role')
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

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['Participant_Name', 'Birth_Date', 'Department', 'Participant_Type']
        widgets = { 
            'Birth_Date': forms.DateInput(attrs={'type': 'date'}), 
        }
