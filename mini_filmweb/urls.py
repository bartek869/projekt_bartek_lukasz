from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView

app_name = 'mini_filmweb'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]

#MovieListView – wyświetla listę wszystkich filmów.
#MovieDetailView – pokazuje szczegóły konkretnego filmu.
#MovieCreateView – umożliwia dodanie nowego filmu.
#MovieUpdateView – umożliwia edycję istniejącego filmu.
#MovieDeleteView – umożliwia usunięcie filmu.