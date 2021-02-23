from .models import GameReview
from django import forms

from django.forms import ModelForm
from django.core.exceptions import ValidationError

class GameReviewAddForm(ModelForm):
	user_score = forms.IntegerField(label="Your Score (0-100):", max_value=100, min_value=0)

	class Meta:
		model = GameReview
		fields = ['user_score']

	