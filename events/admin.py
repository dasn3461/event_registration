from django.contrib import admin
from .models import Event, Registration

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location_name', 'max_slots')
    search_fields = ['title', 'description']
    date_hierarchy = 'date'

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
