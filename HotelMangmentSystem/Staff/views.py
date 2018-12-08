# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Staff
from django.contrib import messages
from django import forms

#viewing existing staff categories , search by staff catogery name


def Staff_view (request):

    query = request.GET.get("q", None)
    staff = Staff.objects.all()

    if query is not None:
        staff = staff.filter(Name__startswith=query)

    context = {
        "Staff": staff,
    }
    return render(request, 'Staff/Staff_view.html', context)


#view employees of this staff catogery , changing status of employee


def Staff_list(request, staff_name):

    employees = Employee.objects.all()
    employees = employees.filter(Staff_name__Name=staff_name)

    query = request.GET.get("q", None)


    if query is not None:
        employees = employees.filter(status__startswith=query)

    if request.method == "POST" and request.user.is_authenticated:

        employee = request.POST.get('employee_name')
        employee_status = request.POST.get('employee_status')
        employee = get_object_or_404(Employee, Name=employee)
        employee.status = employee_status
        employee.save()
    context = {
        "staff_team": employees,
        "staff_name": staff_name,
     }
    return render(request, 'Staff/Staff_list.html', context)




def Receptionist_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and not user.is_superuser:
            login(request, user)
            return HttpResponseRedirect(reverse('Staff_view'))
        else:
            messages.error(request, "Incorrect username or password")
    return render(request, 'Staff/Receptionist_login.html')

def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Staff_view'))



