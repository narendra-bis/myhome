from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	GENRE_CHOICES =(
		('m','male'),
		('f','female')
		)
	MERRITUAL_CHOICES =(
		('mr','merried'),
		('bc', 'bechelor')
		)
	genre=forms.ChoiceField(choices=GENRE_CHOICES)
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
	email = forms.CharField(max_length=40, required=False, help_text='required.valid enmail id')
	birth_date = forms.DateField(help_text='YYYY/MM/DD')
	merritual_staus = forms.ChoiceField(choices=MERRITUAL_CHOICES)


	class Meta:
		model = User
		fields = ('username', 'genre','first_name', 'last_name','email','birth_date','merritual_staus','password1','password2')

