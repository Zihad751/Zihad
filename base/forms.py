from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()
    # file      = forms.FileField()




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

