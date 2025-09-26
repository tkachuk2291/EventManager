from django.urls import path

from event.views import EventUpdateDeleteView, EventListCreateView, EventRegisterManager

urlpatterns = [
    path('events/' , EventListCreateView.as_view(), name="events-list" ),
    path('events/<int:id>/', EventUpdateDeleteView.as_view(), name="events-details"),
    path('events/register/<int:id>/' , EventRegisterManager.as_view() , name="event-register")
]