from django import forms
from .models import *


class CreateStaff(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['Name', 'image', 'salary']


class EditEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Name', 'Email', 'profile_pic', 'Phone',
                  'Address', 'Staff_name']


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Name', 'Email', 'profile_pic', 'Phone',
                  'Address']

