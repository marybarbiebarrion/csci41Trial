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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
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

class Participant(models.Model):
    ID_Number = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    Participant_Name = models.CharField(max_length=100)
    Birth_Date = models.DateField()
    Department = models.CharField(max_length=100)
    PARTICIPANT_TYPES = [
        ('Student', 'Student'),
        ('Faculty', 'Faculty'),
        ('Staff', 'Staff'),
    ]
    Participant_Type = models.CharField(max_length=8, choices=PARTICIPANT_TYPES, default='Student')
 
class Student(models.Model):
    ID_Number = models.OneToOneField(Participant, on_delete=models.CASCADE, primary_key=True)
    Year_Level = models.IntegerField(default=1)
    Program = models.CharField(max_length=100)

class Faculty(models.Model):
    ID_Number = models.OneToOneField(Participant, on_delete=models.CASCADE, primary_key=True)
    Rank = models.CharField(max_length=100)

class Staff(models.Model):
    ID_Number = models.OneToOneField(Participant, on_delete=models.CASCADE, primary_key=True)
    Position = models.CharField(max_length=100)

class UserOrganizer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    organizer = models.OneToOneField(Organizer, on_delete=models.CASCADE)

class Activity(models.Model):
    Activity_ID = models.AutoField(primary_key=True)
    Organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE, related_name='activities')
    Activity_Name = models.CharField(max_length=100)
    Activity_Location = models.CharField(max_length=255)
    Activity_Date = models.DateField()
    Start_Time = models.TimeField()
    End_Time = models.TimeField()

    def __str__(self):
        return self.Activity_Name

class UserParticipant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)