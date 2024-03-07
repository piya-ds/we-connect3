from django.contrib import admin
from .models import UserProfile, Event, Interests, Review

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Interests)
admin.site.register(Review)