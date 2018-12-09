from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Room, Pricing, Date
from .forms import *
# Create your views here.


def admin_login(request):
    if request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_home.html')
    elif request.method == "POST":
        username = request.POST['admin']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {'room': Room, 'price': Pricing, 'date': Date}
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'ownerAdmin/admin_home.html', context)
            else:
                return render(request, 'ownerAdmin/admin_login.html',
                              {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'ownerAdmin/admin_login.html', {'error_message': 'Invalid login'})
    return render(request, 'ownerAdmin/admin_login.html')


def rooms_admin(request):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
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
        return render(request, 'ownerAdmin/rooms_view.html', {'rooms': room_types})


def room_list(request, room_type):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        rooms = Room.objects.all()
        room_list_the_same = []
        room_type_for_header = ''
        for room in rooms:
            room_type_database = room.room_type.replace(" ", "")
            if room_type == room_type_database:
                room_type_for_header = room.room_type
                room_list_the_same.append(room)
        if len(room_list_the_same) == 0:
            return redirect('rooms_admin')
        if request.method == "POST":
            if 'add' in request.POST:
                added_room = Room()
                added_room.room_type = room_list_the_same[0].room_type
                added_room.room_view = room_list_the_same[0].room_view
                added_room.occupation_adult = room_list_the_same[0].occupation_adult
                added_room.occupation_children = room_list_the_same[0].occupation_children
                added_room.room_beds = room_list_the_same[0].room_beds
                added_room.room_size = room_list_the_same[0].room_size
                added_room.room_image = room_list_the_same[0].room_image
                added_room.save()
                return redirect('room_list', room_type)
        return render(request, 'ownerAdmin/room_list.html', {'rooms': room_list_the_same,
                                                             'rooms_number': len(room_list_the_same),
                                                             'room_header': room_type_for_header})


def room_edit(request, room_type, room_id):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        room = get_object_or_404(Room, pk=room_id)
        context = {'room_type': room.room_type, 'room_view': room.room_view,
                   'occupation_adult': room.occupation_adult, 'occupation_children': room.occupation_children,
                   'room_size': room.room_size, 'room_beds': room.room_beds, 'room_number': room.room_number,
                   'room_features_price': room.room_features_price}
        form = EditRoomForm(request.POST or None, request.FILES or None, initial=context)
        if form.is_valid():
            room.room_type = form.cleaned_data.get('room_type')
            room.room_view = form.cleaned_data.get('room_view')
            room.room_beds = form.cleaned_data.get('room_beds')
            room.occupation_children = form.cleaned_data.get('occupation_children')
            room.occupation_adult = form.cleaned_data.get('occupation_adult')
            room.room_size = form.cleaned_data.get('room_size')
            room.room_number = form.cleaned_data.get('room_number')
            room.room_features_price = form.cleaned_data.get('room_features_price')
            room.save()
            return redirect('room_list',  room_type)
        return render(request, 'ownerAdmin/room_edit.html', {'form': form, 'room': room})


def delete_room(request, room_type, room_id):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        if request.method == 'POST':
            if 'delete' in request.POST:
                room = get_object_or_404(Room, pk=room_id)
                room.delete()
                return redirect('room_list', room_type)
            elif 'cancel' in request.POST:
                return redirect('room_list', room_type)
        return render(request, 'ownerAdmin/delete_room.html')


def create_room(request):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        form = CreateRoomForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            room = form.save(commit=False)
            if request.FILES:
                room.room_image = request.FILES['room_image']
            room.save()
            return redirect('rooms_admin')
        return render(request, 'ownerAdmin/create_room.html', {'form': form})


def logout_admin(request):
        logout(request)
        return render(request, 'ownerAdmin/admin_login.html')


def finance_edit(request):
    if not request.user.is_authenticated & request.user.is_superuser:
        return render(request, 'ownerAdmin/admin_login.html')
    else:
        prices = get_object_or_404(Pricing, id=1)
        context = {'bed_price': prices.bed_price, 'breakfast_only_price': prices.breakfast_only_price,
                   'half_board_price': prices.half_board_price, 'full_board_price': prices.full_board_price,
                   'all_inclusive_price': prices.all_inclusive_price, 'is_refundable': prices.is_refundable,
                   'staff_basic_salary': prices.staff_basic_salary}
        form = EditPricing(request.POST or None, request.FILES or None, initial=context)
        if form.is_valid():
            prices.bed_price = form.cleaned_data.get('bed_price')
            prices.breakfast_only_price = form.cleaned_data.get('breakfast_only_price')
            prices.half_board_price = form.cleaned_data.get('half_board_price')
            prices.full_board_price = form.cleaned_data.get('full_board_price')
            prices.all_inclusive_price = form.cleaned_data.get('all_inclusive_price')
            prices.is_refundable = form.cleaned_data.get('is_refundable')
            prices.staff_basic_salary = form.cleaned_data.get('staff_basic_salary')
            prices.save()
    return render(request, 'ownerAdmin/financial_page.html', {'form': form})
