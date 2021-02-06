from django import forms
from .models import *
from django.http import request

class saveCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address'] 

class saveMedicine(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name','price','stock'] 

class saveStock(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['mid','stock'] 