# centralbookings/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Organizer, ContactPerson, Participant, Activity

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

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['Participant_Name', 'Birth_Date', 'Department', 'Participant_Type']
        widgets = { 
            'Birth_Date': forms.DateInput(attrs={'type': 'date'}), 
        }

class ActivityForm(forms.ModelForm):
    Activity_Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Start_Time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    End_Time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Activity
        fields = ['Activity_Name', 'Activity_Location', 'Activity_Date', 'Start_Time', 'End_Time']
