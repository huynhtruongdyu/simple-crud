from django.forms import ModelForm
from django import  forms
from .models import *


class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        widgets  = {
            'type': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'issues': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }


class DesktopForm(ModelForm):
    class Meta:
        model = Desktop
        fields = '__all__'
        widgets  = {
            'type': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'issues': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }


class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        widgets  = {
            'type': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'status': forms.Select(
                attrs={
                    'class':'form-control form-control-sm'
                }
            ),
            'issues': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }


