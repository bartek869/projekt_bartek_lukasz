from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['title', 'description', 'release_year', 'director', 'genres']
    success_url = reverse_lazy('mini_filmweb:movie_list')


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['title', 'description', 'release_year', 'director', 'genres']
    success_url = reverse_lazy('mini_filmweb:movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('mini_filmweb:movie_list')

    #ListView, DetailView itp. stworzone do obsługi podstawowych operacji 
    #template_name – określa, który szablon HTML ma być użyty do wyświetlenia widoku.
    #success_url – URL, do którego przekierowuje po pomyślnym wykonaniu operacji