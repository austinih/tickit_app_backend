from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .serializers import VenueSerializer, EventSerializer, TicketSerializer
from .models import Venue, Event, Ticket
from django.views.generic import View


class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer 
    
class EventVenueDetail(View):
    def get(self, request, venue_pk, event_pk):
        venue = get_object_or_404(Venue, pk=venue_pk)
        event = get_object_or_404(Event, pk=event_pk)
        context = {'venue': venue, 'event': event}
        return render(request, 'event_venue_detail.html', context)
    
class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer 

