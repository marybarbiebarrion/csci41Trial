from django.contrib import admin
from .models import CustomUser, Organizer, UserOrganizer

admin.site.register(CustomUser)
admin.site.register(Organizer)
admin.site.register(UserOrganizer)
