from django.db import models


class Date(models.Model):
    year = models.CharField(max_length=4, null=True)
    month = models.CharField(max_length=2, null=True)
    day = models.CharField(max_length=2, null=True)


class Room(models.Model):
    occupation_adult = models.CharField(max_length=2)
    occupation_children = models.CharField(max_length=2)
    room_type = models.CharField(max_length=15)
    room_view = models.CharField(max_length=10)
    room_size = models.CharField(max_length=2)
    room_date_booked = models.ManyToManyField(Date)
    room_beds = models.IntegerField()

    def __str__(self):
        return self.room_type


class Pricing(models.Model):
    bed_price = models.IntegerField()
    breakfast_only_price = models.IntegerField()
    half_board_price = models.IntegerField()
    full_board_price = models.IntegerField()
    all_inclusive_price = models.IntegerField()
    room_view = models.IntegerField()
    room_type = models.IntegerField()
    is_refundable = models.IntegerField()


