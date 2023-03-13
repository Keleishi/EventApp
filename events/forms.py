from django import forms
from .models import Organizer, Event, Attendee, Category, EventCategory


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'organizer']
