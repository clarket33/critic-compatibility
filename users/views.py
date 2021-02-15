from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to login.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	print("Before validation checks: ", request.user.username)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.user, request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
		
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			
			return redirect('profile')
	else:
		u_form = UserUpdateForm(request.user, instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	
	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)