from django.db import models
from django.contrib.auth.models import User
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class Game(models.Model):
	game_name = models.CharField(max_length=100)
	release_date = models.DateField()
	platform = models.CharField(max_length=100)
	critic_score = models.IntegerField()
	image_src = models.URLField(max_length=300)
	game_src = models.URLField(max_length=300)

	def __str__(self):
		return self.game_name + ", " + self.platform
		'''+ ", " + str(self.critic_score) + ", " + self.image_src + ", " + self.game_src'''

class GameReview(models.Model):
	game_name = models.CharField(max_length=100)
	release_date = models.DateField()
	platform = models.CharField(max_length=100)
	critic_score = models.IntegerField()
	image_src = models.URLField(max_length=300)
	game_src = models.URLField(max_length=300)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	user_score = models.IntegerField()

	def __str__(self):
		return self.game_name + ", " + self.platform + ", " + self.owner.username
		'''+ ", " + str(self.critic_score) + ", " + self.image_src + ", " + self.game_src'''