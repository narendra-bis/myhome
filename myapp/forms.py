from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	email = forms.CharField(max_length=40, required=False, help_text='required.valid enmail id')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','password1','password2')

