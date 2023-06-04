from django.contrib import admin
from .models import UserProfile, Organization, Event

admin.site.register(UserProfile)
admin.site.register(Organization)
admin.site.register(Event)
