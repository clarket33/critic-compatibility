from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	game_name = models.CharField(max_length=100)
	release_date = models.CharField(max_length=20)
	platform = models.CharField(max_length=100)
	critic_score = models.IntegerField()
	image_src = models.URLField(max_length=300)
	game_src = models.URLField(max_length=300)

	def __str__(self):
		return self.game_name + ", " + self.release_date + ", " + self.platform
		'''+ ", " + str(self.critic_score) + ", " + self.image_src + ", " + self.game_src'''

class GameReview(models.Model):
	game_name = models.CharField(max_length=100)
	release_date = models.CharField(max_length=20)
	platform = models.CharField(max_length=100)
	critic_score = models.IntegerField()
	image_src = models.URLField(max_length=300)
	game_src = models.URLField(max_length=300)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	user_score = models.IntegerField()

	def __str__(self):
		return self.game_name + ", " + self.release_date + ", " + self.platform + ", " + self.owner.username
		'''+ ", " + str(self.critic_score) + ", " + self.image_src + ", " + self.game_src'''
