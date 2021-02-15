from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import SearchListView

urlpatterns = [
    path('', views.home, name='games-home'),
    path('search', login_required(SearchListView.as_view()), name='games-search')
]
