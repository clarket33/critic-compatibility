import django_tables2 as tables
from .models import Game

class GameTable(tables.Table):
    class Meta:
        model = Game
        template_name = "django_tables2/semantic.html"
        fields = ("game_name", "release_date", "platform")