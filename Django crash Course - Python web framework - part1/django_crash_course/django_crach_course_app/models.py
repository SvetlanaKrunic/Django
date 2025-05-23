from django.db import models

# Create your models here.
class MenuItems(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now = True)
    comment = models.CharField(max_length = 1000)
    

