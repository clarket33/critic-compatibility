from .models import GameReview
from django import forms

from django.forms import ModelForm
from django.core.exceptions import ValidationError

class GameReviewAddForm(ModelForm):
	user_score = forms.IntegerField(label="Your Score", max_value=100, min_value=0)

	class Meta:
		model = GameReview
		fields = ['user_score']

	def clean_user_score(self):
		user_score = self.cleaned_data["user_score"]

		if user_score < 0 or user_score > 100:
			raise ValidationError("Score must be between 0-100")
		return user_score