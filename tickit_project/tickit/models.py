from django.db import models



class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image_url = models.TextField()

    def __str__(self):
        return self.name
    
    
class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100, default='no event title')
    artist = models.CharField(max_length=100, default='no artist title')
    date = models.DateField(null=True)
    genre = models.CharField(max_length=100, default='no genre title')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image_url = models.TextField(default='default_image_url')

    def __str__(self):
        return self.title


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=100, default='no ticket name')
    email = models.CharField(max_length=100, default='no ticket email')
    phone_number = models.CharField(max_length=20, default='no phone number')
    seat_number = models.CharField(max_length=10, blank=True)
    credit_card_number = models.CharField(max_length=20, default='0')

    def __str__(self):
        return self.name

       
