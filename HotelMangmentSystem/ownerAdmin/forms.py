from django import forms
from .models import Room


class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_view', 'occupation_adult', 'occupation_children', 'room_size', 'room_beds',
                  'room_number']


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_view', 'occupation_adult', 'occupation_children', 'room_size', 'room_beds',
                  'room_image', 'room_number']
