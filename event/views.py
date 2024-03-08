from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event/index.html'
    paginate_by = 6
    context_object_name = 'events'  # Plural name for a list of events
    # context_object_name = 'events'  # Plural name for a list of events

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

# class MyEventView(View):
#     def get(self, request, *args, **kwargs):
#         # Example: Retrieve events that occurred after a specific date
#         my_events = Event.objects.filter(date__gte='2022-01-01')

#         return render(request, 'event/my_event_template.html', context={'my_events': my_events})
