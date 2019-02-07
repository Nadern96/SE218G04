from django.urls import path
from booking import views
from django.conf import settings
from django.conf.urls.static import static
from ownerAdmin.models import Room

urlpatterns = [
    path('', views.book, name='book'),
    path('form/', views.form, name='form'),
    path('search/form', views.form, name='form'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),

]