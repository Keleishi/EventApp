# Create your models here.
from django.db import models


# Model for the Organizer table
class Organizer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Model for the Event table
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Model for the Attendee table
class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Model for the Category table
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Model for the EventCategory table
class EventCategory(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.name} - {self.category.name}"
