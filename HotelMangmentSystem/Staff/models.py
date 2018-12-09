from django.db import models

from django.contrib.auth.models import Permission, User
from django.utils import timezone

# Create your models here.


class Staff(models.Model):
    Name = models.CharField(max_length=100)
    image = models.FileField(null=True)
    salary = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name


class Employee(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    profile_pic = models.FileField(null=True)
    status = models.CharField(max_length=20, default='Status')
    time = models.TimeField(default=timezone.now())
    Phone = models.CharField(max_length=14)
    Address = models.CharField(max_length=100, default='7 Address Hotel')
    Staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = ['time']

    def __str__(self):
        return self.Name



