from django.contrib import admin

from .models import Event, EventCategory, Category, Organizer

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Category)
admin.site.register(Organizer)