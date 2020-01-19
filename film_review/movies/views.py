from django.shortcuts import render

from django.views.generic.base import View
from .models import Movie

class MoviesView(View):
	'''List of movie'''
	def get(self, request):
		movies = Movie.objects.all()
		data = {'movie_list': movies}
		return render(request, 'movies/movie_list.html' context=data)