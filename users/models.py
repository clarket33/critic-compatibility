from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
	IMG_CHOICES = (
		('media/profile_pics/Blue.png', 'Blue'),
		('media/profile_pics/Green.png', 'Green'),
		('media/profile_pics/Purple.png', 'Purple'),
		('media/profile_pics/Pink.png', 'Pink'),
		('media/profile_pics/Yellow.png', 'Yellow'),
		('media/profile_pics/Red.png', 'Red'),
		('media/profile_pics/Orange.png', 'Orange')

	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.CharField(max_length=100, choices=IMG_CHOICES, default='media/profile_pics/Blue.png')


	def __str__(self):
		return f'{self.user.username}\'s Profile'

	def save(self, *args, **kwargs):
    		super().save(*args, **kwargs)

