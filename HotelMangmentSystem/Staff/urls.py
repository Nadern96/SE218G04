from django.urls import path
from Staff import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Staff_view, name='Staff_view'),
    path('create_staff', views.create_staff, name="create_staff"),
    path('<staff_name>/AddEmployee', views.add_employee, name="add_employee"),
    path('<staff_name>/', views.Staff_list, name='Staff_list'),
    path('<staff_name>/edit', views.edit_staff, name='edit_staff'),
    path('<staff_name>/delete', views.delete_staff, name='delete_staff'),
    path('<staff_name>/<employee_name>/edit', views.edit_employee, name='edit_employee'),
    path('<staff_name>/<employee_name>/delete', views.delete_employee, name='delete_employee'),
    path('logout', views.User_logout, name='User_logout'),
    path('receptionist_login', views.Receptionist_login, name="Receptionist_login"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
