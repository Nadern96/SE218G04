from django.conf.urls import url
from ownerAdmin import views

urlpatterns = [
    url(r'^$', views.admin_login, name='admin_login'),
]
