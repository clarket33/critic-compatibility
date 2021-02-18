import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):

	PLATFORM_CHOICES = (
		('3DS', '3DS'),
		('DS', 'DS'),
		('Dreamcast', 'Dreamcast'),
		('Game Boy Advance', 'Game Boy Advance'),
		('GameCube', 'GameCube'),
		('Nintendo 64', 'Nintendo 64'),
		('PC', 'PC'),
		('PSP', 'PSP'),
		('PlayStation 5', 'PlayStation 5'),
		('PlayStation 4', 'PlayStation 4'),
		('PlayStation 3', 'PlayStation 3'),
		('PlayStation 2', 'PlayStation 2'),
		('PlayStation', 'PlayStation'),
		('PlayStation Vita', 'PlayStation Vita'),
		('Stadia', 'Stadia'),
		('Switch', 'Switch'),
		('Wii U', 'Wii U'),
		('Wii', 'Wii'),
		('Xbox Series X', 'Xbox Series X'),
		('Xbox One', 'Xbox One'),
		('Xbox 360', 'Xbox 360'),
		('Xbox', 'Xbox')
	)


	game_name = django_filters.CharFilter(label='Title: ', lookup_expr='contains')
	platform = django_filters.ChoiceFilter(label='Platform: ',choices=PLATFORM_CHOICES)


	class Meta:
		model = Game
		fields = ['game_name', 'platform']


'''
Platforms:
{'Xbox', 'Game Boy Advance', 'Xbox 360', 'PlayStation Vita',
 'Wii', 'Stadia', 'PlayStation 2', 'PlayStation 3', 'Switch', 'DS', 'PC', 
 'Nintendo 64', 'PSP', 'Xbox Series X',
 'Wii U', 'PlayStation 4', 'PlayStation', 'Xbox One', '3DS', 'PlayStation 5', 'Dreamcast', 'GameCube'}
'''