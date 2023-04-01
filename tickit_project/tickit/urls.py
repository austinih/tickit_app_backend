from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.VenueList.as_view(), name='venue_list'),
    path('venues', views.VenueList.as_view(), name='venue_list'),
    path('events', views.EventList.as_view(), name='event_list'),
    path('tickets', views.TicketList.as_view(), name='ticket_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue_detail'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('tickets/<int:pk>', views.TicketDetail.as_view(), name='ticket_detail'),
    path('venues/<int:venue_pk>/events/<int:event_pk>', views.EventVenueDetail.as_view(), name='event_venue_detail')

]

