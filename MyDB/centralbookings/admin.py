from django.contrib import admin
from .models import CustomUser, Organizer, UserOrganizer, Participant, UserParticipant

admin.site.register(CustomUser)
admin.site.register(Organizer)
admin.site.register(UserOrganizer)
admin.site.register(Participant)
admin.site.register(UserParticipant)
