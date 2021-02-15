from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameReview


# Create your views here.
@login_required
def home(request):
	
	context = {
		'gameReviews': request.user.gamereview_set.all()
	}
	return render(request, 'games/home.html', context)
	

'''
Platforms:
{'Xbox', 'Game Boy Advance', 'Xbox 360', 'PlayStation Vita',
 'Wii', 'Stadia', 'PlayStation 2', 'PlayStation 3', 'Switch', 'DS', 'PC', 
 'Nintendo 64', 'PSP', 'Xbox Series X',
 'Wii U', 'PlayStation 4', 'PlayStation', 'Xbox One', '3DS', 'PlayStation 5', 'Dreamcast', 'GameCube'}
'''