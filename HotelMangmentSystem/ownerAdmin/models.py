from django.db import models
from django.contrib.auth.models import Permission, User


class Date(models.Model):
    date = models.CharField(max_length=20, default="ok")


class Room(models.Model):
    occupation_adult = models.CharField(max_length=2)
    occupation_children = models.CharField(max_length=2)
    room_type = models.CharField(max_length=15)
    room_view = models.CharField(max_length=10)
    room_size = models.CharField(max_length=2)
    room_date_booked = models.ManyToManyField(Date, blank=True)
    room_beds = models.IntegerField(blank=True, null=True)
    room_image = models.ImageField(blank=True, null=True, upload_to="roomImages", default='roomImages/room3.jpg')
    room_number = models.CharField(max_length=20)
    room_features_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.room_type.replace(" ", "")


class Pricing(models.Model):
    bed_price = models.IntegerField(blank=True, null=True)
    breakfast_only_price = models.IntegerField(blank=True, null=True)
    half_board_price = models.IntegerField(blank=True, null=True)
    full_board_price = models.IntegerField(blank=True, null=True)
    all_inclusive_price = models.IntegerField(blank=True, null=True)
    is_refundable = models.IntegerField(blank=True, null=True)
    staff_basic_salary = models.IntegerField(blank=True, null=True)


