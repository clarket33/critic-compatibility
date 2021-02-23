from django.contrib import admin
from .models import Game, GameReview, CriticProfile, CriticReview

admin.site.register(Game)
admin.site.register(GameReview)
admin.site.register(CriticProfile)
admin.site.register(CriticReview)