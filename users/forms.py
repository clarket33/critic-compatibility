from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email already exists")
		return email

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(UserUpdateForm, self).__init__(*args, **kwargs)

	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			if(User.objects.filter(email=email).first().username != self.user.username):
					raise ValidationError("An account is already associated with this email")

		return email

	def clean_username(self):
		username = self.cleaned_data['username']

		if User.objects.filter(username=username).exists():
			if(User.objects.filter(username=username).first().username != self.user.username):
					raise ValidationError("This username is already in use")

		return username



	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']