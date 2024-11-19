from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser): 
    PARTICIPANT = 'participant' 
    ORGANIZER = 'organizer' 
    
    ROLE_CHOICES = [ 
        (PARTICIPANT, 'Participant'), 
        (ORGANIZER, 'Organizer'), 
    ] 
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

class Organizer(models.Model):
    ORGANIZER_TYPES = [
        ('Internal', 'Internal'),
        ('External', 'External'),
    ]
    Organizer_ID = models.AutoField(primary_key=True)
    Organizer_Name = models.CharField(max_length=100)
    Organizer_Address = models.CharField(max_length=255)
    Organizer_Type = models.CharField(max_length=8, choices=ORGANIZER_TYPES, default='Internal')

class Internal(models.Model):
    Organizer_ID = models.OneToOneField(Organizer, on_delete=models.CASCADE, primary_key=True)
    Organizer_Department = models.CharField(max_length=100)

class External(models.Model):
    Organizer_ID = models.OneToOneField(Organizer, on_delete=models.CASCADE, primary_key=True)
    Organization_Name = models.CharField(max_length=100)

class ContactPerson(models.Model):
    Organizer_ID = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    Contact_Name = models.CharField(max_length=100)
    Contact_Email = models.EmailField(max_length=100)
    Contact_Number = models.CharField(max_length=12)
