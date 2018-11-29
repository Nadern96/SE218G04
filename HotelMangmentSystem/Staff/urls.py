from django.urls import path
from Staff import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Staff_view, name='Staff_view'),
    path('<staff_name>/', views.Staff_list, name='Staff_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
