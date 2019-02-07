from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from ownerAdmin.models import Room

urlpatterns = [
       path('', views.Home, name='Home'),
]