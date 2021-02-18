from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import FilteredSearchListView

urlpatterns = [
    path('', views.home, name='games-home'),
    path('search', login_required(FilteredSearchListView.as_view()), name='games-search'),
    path('search/<int:pk>/', views.gameAdd, name='game-add'),
    path('<int:pk>/delete', views.deleteGame, name='game-delete')
]
