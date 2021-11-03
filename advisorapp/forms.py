from .models import addadvisor
from .models import advdisplay

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateAdvisors(forms.ModelForm):
    class Meta:
        model = addadvisor
        # fields = '__all__'
        fields = ['advname','profilepic']


class FilterForm(forms.Form):
    class Meta:
        model = advdisplay
        fields = ['id','advname','profilepic','bookingid','bookingtime']
