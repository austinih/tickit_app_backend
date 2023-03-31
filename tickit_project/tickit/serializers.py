from rest_framework import serializers

from .models import Venue, Event, Ticket


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        read_only=True
    )
    
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event'
    )
    
    class Meta:
        model = Ticket
        fields = ('id', 'event', 'event_id', 'name', 'email', 'phone_number', 'seat_number', 'credit_card_number')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )
    
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )
    
    class Meta:
        model = Event
        fields = ('id', 'artist', 'title', 'venue', 'venue_id', 'date', 'price', 'genre')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event = EventSerializer(
        many=True,
        read_only=True
    )
    
    venue = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'image_url', 'event', 'venue')

