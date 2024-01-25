from django.forms import ModelForm
from django.contrib.auth.models import User
from basic_app import models
from django import forms

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ["username", "email", "password"]
		widgets = {'password': forms.PasswordInput}

class UserProfileInfoForm(ModelForm):
	class Meta:
		model = models.UserProfileInfo
		fields = ["portfolio_site", "profile_pic"] 
