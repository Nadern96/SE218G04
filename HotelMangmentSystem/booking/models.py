from django.db import models

# Create your models here.

class booking(models.Model):
    customer_name = models.CharField(max_length=30)
    checkin = models.DateField(default=None)
    checkout = models.DateField(default=None)
    room = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.customer_name + "  " + self.room + "  " + self.booking_day + "/" + self.booking_month + "/" + self.booking_year
