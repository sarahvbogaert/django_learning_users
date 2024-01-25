from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basic_app import forms

# Create your views here.

def register(request):
	if request.method == "POST":
		user_form = forms.UserForm(request.POST)
		user_profile_info_form = forms.UserProfileInfoForm(request.POST, files=request.FILES)
		if user_form.is_valid() and user_profile_info_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = user_profile_info_form.save(commit = False)
			profile.user = user
			user_profile_info_form.save()
			print(profile.profile_pic)
			return render(request, "basic_app/register_success.html")
	else:
		user_form = forms.UserForm()
		user_profile_info_form = forms.UserProfileInfoForm()
	context_dict = {'user_form': user_form, 'user_profile_info_form': user_profile_info_form}
	return render(request, "basic_app/register_form.html", context_dict)

@login_required
def special(request):
	return render(request, "basic_app/special.html")

