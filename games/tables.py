import django_tables2 as tables
from .models import Game
from django_tables2.utils import A

class GameTable(tables.Table):

	game_name = tables.Column(verbose_name= 'Title')
	release_date = tables.Column(verbose_name= 'Release Date')
	add = tables.TemplateColumn(verbose_name='',template_name="games/add_column.html", orderable=False)
	#add = tables.LinkColumn('game-add', args=[A('pk')], orderable = False, empty_values=())

	class Meta:
		model = Game
		template_name = "django_tables2/bootstrap.html"
		fields = ("game_name", "release_date", "platform")
		order_by = "-release_date"
