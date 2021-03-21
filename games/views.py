from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import GameReview, Game, CriticProfile, CriticReview
from .filters import GameFilter
from .tables import GameTable
from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .forms import GameReviewAddForm
from django.contrib import messages
from django.shortcuts import render, redirect
from collections import OrderedDict
from django.template.defaulttags import register
from django.core.paginator import Paginator



#user Game review inventory
@login_required
def home(request):
	gameReviews = request.user.gamereview_set.all()
	paginator = Paginator(gameReviews, 10)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'gameReviews': page_obj
	}
	return render(request, 'games/home.html', context)

#table view of the games	
class FilteredSearchListView(SingleTableMixin, FilterView):
    table_class = GameTable
    model = Game
    template_name ='games/search.html'
    filterset_class = GameFilter

#user is adding a game review
@login_required
def gameAdd(request, pk):
	#obtain game being added
	g = get_object_or_404(Game, pk=pk)

	#check if game has already been added
	if len(GameReview.objects.filter(game_name=g.game_name).filter(platform=g.platform)
		.filter(owner=request.user)) != 0:
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

#user is deleting a game review
@login_required
def deleteGame(request, pk):

	gr = get_object_or_404(GameReview, pk=pk)

	#check to make sure current user is the one with that review
	if gr.owner != request.user:
		messages.error(request, f"You don't have access to that game score")
		return redirect('games-home')

	if request.method == "POST":
		gr.delete()
		messages.success(request, f"Deleted Score for '{gr.game_name}'!")
		return redirect('games-home')

	

	context = {
		'game_review': gr
	}
	return render(request, 'games/delete_game.html', context)

#match user with compatible critics
@login_required
def criticMatch(request):


	@register.filter
	def get_item(dictionary, key):
		return dictionary.get(key)


	my_games = request.user.gamereview_set.all()
	compat = dict()
	
	for gameR in my_games:
		
		for critReview in CriticReview.objects.filter(game_name=gameR.game_name).filter(platform=gameR.platform):
			curCrit = critReview.critic.critic_name

			if (curCrit) in compat:
				compat[curCrit][0] += abs(critReview.critic_score-gameR.user_score)
				compat[curCrit][1] += 1
			else:
				compat[curCrit] = [abs(critReview.critic_score-gameR.user_score),1]


	#print(compat)


	for key in list(compat):
		#subject to change, sets min mutual games (maybe allow for user input)
		if compat[key][1] <= 4:
			del compat[key]
			continue
		compat[key][0] = round(compat[key][0] / compat[key][1], 2)




	odCompat = OrderedDict(sorted(compat.items(), key=lambda x:x[1]))

	'''
	i = 0;
	for key, value in odCompat.items():
		if i > 5:
			break
		if value[1] >= 5:
			print(key, value)
			i+=1
	'''

	while len(odCompat) > 10:
		odCompat.popitem()

	profiles = dict()
	for key, value in odCompat.items():
		profiles[key] = CriticProfile.objects.filter(critic_name=key).first().critic_src

		'''
	for key, value in profiles.items():
		print(key, value)
		
	'''
			

	#print(odCompat)

	context = {
		'compatRanks': odCompat,
		'gameAmnt': len(request.user.gamereview_set.all()),
		'criticProfs': profiles
	}

	return render(request, 'games/critic_match.html', context)
'''
Platforms:
{'Xbox', 'Game Boy Advance', 'Xbox 360', 'PlayStation Vita',
 'Wii', 'Stadia', 'PlayStation 2', 'PlayStation 3', 'Switch', 'DS', 'PC', 
 'Nintendo 64', 'PSP', 'Xbox Series X',
 'Wii U', 'PlayStation 4', 'PlayStation', 'Xbox One', '3DS', 'PlayStation 5', 'Dreamcast', 'GameCube'}
'''