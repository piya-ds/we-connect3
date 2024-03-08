from django.urls import path
from .views import EventListView, EventDetailView
# from .views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='events-list'),
    path('event_detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    # path('my_event/', MyEventView.as_view(), name='my-event'),
]


