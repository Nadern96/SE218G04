from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Employee , Staff

def Staff_view (request):
    staff = Staff.objects.all()
    context = {
        "Staff": staff,
    }

    return render(request, 'Staff/Staff_view.html', context)

def Staff_list (request,staff_name):
    employees = Employee.objects.all()
    employees = employees.filter(Staff_name__Name=staff_name)
    context = {
        "staff_team": employees,
        "staff_name": staff_name,

     }
    return render(request, 'Staff/Staff_list.html', context)
