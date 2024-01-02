from django import forms
from django.utils import timezone
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location_name', 'max_slots']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError("The date cannot be in the past.")
        return date

    def clean_max_slots(self):
        max_slots = self.cleaned_data['max_slots']
        if max_slots <= 0:
            raise forms.ValidationError("Maximum slots must be a positive number.")
        return max_slots
