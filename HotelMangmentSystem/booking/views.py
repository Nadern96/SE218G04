from datetime import date
from dateutil import parser


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
    return render(request, 'Booking.html',{'rooms': room_types,'room_type_filter':room_type_filter})




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


    return render(request, 'Booking.html',{'rooms': room_types,'room_type_filter':room_type_filter})


def form(request):
    room = request.GET.get('room')
    return render(request, 'form.html')



def register(request):
    name = request.GET.get('name')
    tel = request.GET.get('tel')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    ''' checks in date format'''
    checkin_date = parser.parse (checkin)
    checkout_date =  parser.parse (checkout)
    dif = checkout_date - checkin_date



    customer_reg = booking()
    customer_reg.customer_name=name
    customer_reg.checkin= checkin_date
    customer_reg.checkout=checkout_date

    DateToBeSaved = Date()

    for x in range(checkin_date , checkout_date):
        if x in Date.objects.all:
            continue
        else:
            DateToBeSaved=x
            DateToBeSaved.save()


    RoomsToBeReserved = Room.objects.filter(room_type=request.GET.get('room'))
    ChossenRoom = [room for room in RoomsToBeReserved
                    if range(checkin_date, checkout_date) not in RoomsToBeReserved.room_date_booked]
    if ChossenRoom is None :
        '''return not exisr'''
    else:


        return HttpResponse("<h1>"+name+" "+tel+" "+checkin+" "+checkout+"the time is "+dif.__str__() +"</h1>")



def homepage (request):
    return render(request, 'home.html')