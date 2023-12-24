from django import forms
from .models import *


class AddLoginForm(forms.Form):
    login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "log", "placeholder": "Login"}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "password",
                                                                             "placeholder": "Password"}))


class AddRegisterForm(forms.Form):
    login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "log", "placeholder": "Login"}))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "password",
                                                                              "placeholder": "Password"}))
    sfc = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"type": "sfc", "placeholder": "Your SFC"}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"type": "address",
                                                                            "placeholder": "Address"}))
    phone_num = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={"type": "phone_num",
                                                                              "placeholder": "Phone Number"}))


class AppointmentForm(forms.Form):
    meet_time = forms.DateTimeField(widget=forms.TextInput(attrs={"type": "datetime-local",
                                                                  "id": "localdate", "name": "date"}))


class AppointmentForm2(forms.Form):
    customer = forms.IntegerField()
    tutor = forms.IntegerField()
    meet_time = forms.DateTimeField()
    homework = forms.CharField()


class AddTutProf(forms.Form):
    prof = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Enter Your Profession"}))


class HomeForm(forms.Form):
    home = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Enter new homework"}))
