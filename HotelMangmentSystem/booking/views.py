from datetime import date
from dateutil import parser
from datetime import date, timedelta
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from ownerAdmin.models import Room
from .models import booking
from ownerAdmin.models import Date
from ownerAdmin.models import Pricing


# room in Room:
#   return HttpResponse("<h1> " + room.room_number + "</h1>")


# Create your views here.

def book(request):
    room_types = []
    rooms = Room.objects.all()
    for room in rooms:
        global found
        found = False
        if len(room_types) == 0:
            room_types.append(room)
        else:
            for room_type in room_types:
                if room.room_type == room_type.room_type:
                    found = True
                    break
            if not found:
                room_types.append(room)
    room_type_filter = room_types
    return render(request, 'booking.html',{'rooms': room_types,'room_type_filter':room_type_filter})




def search(request):
    room_types_search = request.GET.get('room_types')
    roombed = request.GET.get('room_bed')
    room_types = []
    rooms = Room.objects.all()
    for room in rooms:
        global found
        found = False
        if len(room_types) == 0:
            room_types.append(room)
        else:
            for room_type in room_types:
                if room.room_type == room_type.room_type:
                    found = True
                    break
            if not found:
                room_types.append(room)

    room_type_filter = room_types.copy()

    if(room_types_search==""):
         room_type_filter = [room for room in room_type_filter]
    else:
        room_type_filter = [ room for room in room_type_filter if room.room_type ==room_types_search ]


    return render(request, 'booking.html',{'rooms': room_types,'room_type_filter':room_type_filter})


def form(request):
   room = Room.objects.filter(room_type=request.GET.get('room'))
   priceing = Pricing.objects.all()
   price = priceing[0].bed_price + priceing[0].all_inclusive_price
   return render(request, 'form.html', {'room': room[0], 'price': price})

def date_range(start_date, end_date):
    for ordinal in range(start_date.toordinal(), end_date.toordinal()):
        yield datetime.date.fromordinal(ordinal)


def register(request):
    name = request.GET.get('username')
    tel = request.GET.get('usrtel')
    checkin =parser.parse (request.GET.get('check in'))
    checkout = parser.parse (request.GET.get('check out'))
    dif = checkout - checkin
    room_type=request.GET.get('room')
    rooms = Room.objects.filter(room_type__contains="s")

    start=checkin

    dates = []
    step = datetime.timedelta(days=1)
    while start <= checkout:
        dates.append(start.date())
        start += step


    for room in rooms:
        result = all(elem in dates for elem in room.room_date_booked.all() )
        if result:

            new = booking()
            new.room=room.room_number
            new.customer_name=name
            new.checkin = checkin
            new.checkout = checkout
            new.save()
            return HttpResponse("<h1>done<h1>")
        else:
            return HttpResponse("<h1>notfound<h1>")




    return HttpResponse("<h1>"+name+" "+tel+" "+checkin.date().__str__()+" "+checkout.date().__str__()+"the time is "+dif.__str__() +"   date "+dates.__str__()+"</h1>")


