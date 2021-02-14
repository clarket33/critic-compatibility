from django.shortcuts import render
from django.http import HttpResponse
from .models import GameReview


# Create your views here.
def home(request):
	context = {
		'gameReviews': GameReview.objects.all()
	}
	return render(request, 'games/home.html', context)

'''
Platforms:
{'Xbox', 'Game Boy Advance', 'Xbox 360', 'PlayStation Vita',
 'Wii', 'Stadia', 'PlayStation 2', 'PlayStation 3', 'Switch', 'DS', 'PC', 
 'Nintendo 64', 'PSP', 'Xbox Series X',
 'Wii U', 'PlayStation 4', 'PlayStation', 'Xbox One', '3DS', 'PlayStation 5', 'Dreamcast', 'GameCube'}
'''