from django import forms
from .models import Room, Pricing


class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_view', 'occupation_adult', 'occupation_children', 'room_size', 'room_beds',
                  'room_number']


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'room_view', 'occupation_adult', 'occupation_children', 'room_size', 'room_beds',
                  'room_image', 'room_number', 'room_features_price']


class EditPricing(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['bed_price', 'breakfast_only_price', 'half_board_price', 'full_board_price', 'all_inclusive_price',
                  'is_refundable', 'staff_basic_salary']