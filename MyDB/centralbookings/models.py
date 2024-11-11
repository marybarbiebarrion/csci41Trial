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