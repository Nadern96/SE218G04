from django.urls import path
from ownerAdmin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('rooms', views.rooms_admin, name='rooms_admin'),
    path('financial', views.finance_edit, name='finance_edit'),
    path('rooms/<slug:room_type>', views.room_list, name='room_list'),
    path('rooms/<slug:room_type>/<int:room_id>', views.room_edit, name='room_edit'),
    path('rooms/<slug:room_type>/<int:room_id>/delete', views.delete_room, name='delete_room'),
    path('rooms/create/room', views.create_room, name='create_room'),
    path('logout', views.logout_admin, name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
