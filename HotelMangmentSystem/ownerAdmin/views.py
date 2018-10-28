from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Room,Pricing,Date
# Create your views here.


def admin_login(request):
    if request.method == "POST":
        username = request.POST['admin']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {'room': Room, 'price': Pricing, 'date': Date}
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'ownerAdmin/admin_index.html', context)
            else:
                return render(request, 'ownerAdmin/admin_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'ownerAdmin/admin_login.html', {'error_message': 'Invalid login'})
    return render(request, 'ownerAdmin/admin_login.html')

