from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Organizer, UserOrganizer, Participant, UserParticipant

# Signal to create UserOrganizer when an Organizer is created
@receiver(post_save, sender=Organizer)
def create_user_organizer(sender, instance, created, **kwargs):
    if created:
        UserOrganizer.objects.create(user=instance.user, organizer=instance)

# Signal to create UserParticipant when a Participant is created
@receiver(post_save, sender=Participant)
def create_user_participant(sender, instance, created, **kwargs):
    if created:
        UserParticipant.objects.create(user=instance.user, participant=instance)
