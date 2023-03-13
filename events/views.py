from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Organizer, Event, Attendee, Category, EventCategory
from .forms import EventForm


# View function for the home page
def home(request):
    return render(request, 'home.html')


# View function for creating a new event
def event_create(request):
    # If the request is a POST request
    if request.method == 'POST':
        # Create a new EventForm with the data from the form
        form = EventForm(request.POST)
        # If the form is valid, save the new event and redirect to the event list page
        if form.is_valid():
            form.save()
            return redirect('event_list')
    # If the request is not a POST request, create a new empty EventForm
    else:
        form = EventForm()
    # Render the event creation page with the EventForm
    return render(request, 'event_create.html', {'form': form})


# View function for listing all events
def event_list(request):
    # Get all events from the database
    events = Event.objects.all()
    # Render the event list page with the list of events
    return render(request, 'event_list.html', {'events': events})


# View function for showing the details of a single event
def event_detail(request, pk):
    # Get the event with the specified primary key from the database
    event = get_object_or_404(Event, pk=pk)
    # Render the event detail page with the event
    return render(request, 'event_detail.html', {'event': event})


# View function for updating an event
def event_update(request, pk):
    # Get the event with the specified primary key from the database
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        # Create a new EventForm with the data from the form and the existing event
        form = EventForm(request.POST, instance=event)
        # If the form is valid, save and redirect to the event detail page
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    # Else, create a new EventForm with the existing event
    else:
        form = EventForm(instance=event)

    # Render the event update page with the EventForm
    return render(request, 'event_update.html', {'form': form})


# View function for deleting an existing event
def event_delete(request, pk):
    # Get the event with the specified primary key from the database
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        # Delete the event from the database and redirect to the event list page
        event.delete()
        return redirect('event_list')

    # Render the event delete confirmation page with the event
    return render(request, 'event_delete.html', {'event': event})