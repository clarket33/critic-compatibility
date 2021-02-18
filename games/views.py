from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameReview, Game
from .filters import GameFilter
from .tables import GameTable
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .forms import GameReviewAddForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
@login_required
def home(request):
	
	context = {
		'gameReviews': request.user.gamereview_set.all()
	}
	return render(request, 'games/home.html', context)


	
class FilteredSearchListView(SingleTableMixin, FilterView):
    table_class = GameTable
    model = Game
    template_name ='games/search.html'

    filterset_class = GameFilter

@login_required
def gameAdd(request, pk):
	#obtain game being added
	g = get_object_or_404(Game, pk=pk)

	#check if game has already been added
	if len(GameReview.objects.filter(game_name=g.game_name).filter(release_date=g.release_date)
		.filter(platform=g.platform).filter(owner=request.user)) != 0:
		messages.error(request, f"You've already scored '{g.game_name}'")
		return redirect('games-search')

	#convert to a GameReview since that is what it's being saved as
	gr = GameReview(game_name=g.game_name, release_date=g.release_date, platform=g.platform,
		critic_score=g.critic_score, image_src=g.image_src, game_src=g.game_src, owner=request.user,
		user_score='')

	if request.method == 'POST':
		form = GameReviewAddForm(request.POST, instance=gr)
		if form.is_valid():
			form.save()
			messages.success(request, f"Added '{g.game_name}'!")
			return redirect('games-search')
	else:
		form = GameReviewAddForm(instance=gr)
	context = {
		'cur_game': g,
		'form': form
	}

	return render(request, 'games/game_detail.html', context)

@login_required
def deleteGame(request, pk):

	gr = get_object_or_404(GameReview, pk=pk)

	#check to make sure current user is the one with that review
	if gr.owner != request.user:
		messages.error(request, f"You don't have access to that game score")
		return redirect('games-home')

	if request.method == "POST":
		gr.delete()
		return redirect('games-home')

	

	context = {
		'game_review': gr
	}
	return render(request, 'games/delete_game.html', context)




'''
Platforms:
{'Xbox', 'Game Boy Advance', 'Xbox 360', 'PlayStation Vita',
 'Wii', 'Stadia', 'PlayStation 2', 'PlayStation 3', 'Switch', 'DS', 'PC', 
 'Nintendo 64', 'PSP', 'Xbox Series X',
 'Wii U', 'PlayStation 4', 'PlayStation', 'Xbox One', '3DS', 'PlayStation 5', 'Dreamcast', 'GameCube'}
'''