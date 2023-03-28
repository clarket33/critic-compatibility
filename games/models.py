from django.db import models
from django.contrib.auth.models import User
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

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

class Game(models.Model):
	game_name = models.CharField(max_length=100)
	release_date = models.DateField()
	platform = models.CharField(max_length=100, choices = PLATFORM_CHOICES)
	metascore = models.IntegerField()
	image_src = models.URLField(max_length=300)
	game_src = models.URLField(max_length=300)

	def __str__(self):
		return self.game_name + ", " + self.platform

	class Meta:
		unique_together = [['game_name', 'platform']]

class GameReview(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	user_score = models.IntegerField()

	def __str__(self):
		return self.game.game_name + ", " + self.game.platform + ", " + self.owner.username
		'''+ ", " + str(self.critic_score) + ", " + self.image_src + ", " + self.game_src'''

	class Meta:
		unique_together = [['game', 'owner']]

class CriticProfile(models.Model):
	critic_name = models.CharField(max_length=100)
	critic_src = models.URLField(max_length=300)

	def __str__(self):
		return self.critic_name

	class Meta:
		unique_together = [['critic_name']]

class CriticReview(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	critic = models.ForeignKey(CriticProfile, on_delete=models.CASCADE)
	critic_score = models.IntegerField()

	def __str__(self):
		return self.game.game_name + ", " + str(self.game.metascore) + ", " + self.game.platform + ", " + self.critic.critic_name

	class Meta:
		unique_together = [['game', 'critic']]