from django.db import models
from datetime import date


# Create your models here.


class Category(models.Model):
	'''Категории'''
	name = models.CharField('Категория', max_length=150)
	description = models.TextField('Описание')
	url = models.SlugField(max_length=150)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Actors(models.Model):
	''' Актеры и режиссеры'''
	name = models.CharField('Имя', max_length= 150)
	age = models.PositiveSmallIntegerField('Возраст', default=0)
	description = models.TextField('Описание')
	image = models.ImageField('Изображение', upload_to='actors/')


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Актеры и режиссеры'
		verbose_name_plural = 'Актеры и режиссеры'

class Genre(models.Model):
	'''Жанры'''

	name = models.CharField('Имя', max_length=100)
	description = models.TextField('Описание', max_length=3000)
	url = models.SlugField(max_length=160, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'

class Movie(models.Model):
	'''Фильмы'''
	title = models.CharField('Название' ,max_length=100)
	tagline = models.CharField('Слоган', max_length=100)
	description = models.TextField('Описание' )
	poster = models.ImageField('Постер', upload_to='movies/')
	year = models.PositiveSmallIntegerField('Дата выхода', default= 2020)
	country = models.CharField('Страна', max_length=60)
	directors= models.ManyToManyField(Actors, verbose_name='режиссер', related_name='film_director')
	actors = models.ManyToManyField(Actors, verbose_name='Актеры', related_name='film_actor')
	genres = models.ManyToManyField(Genre, verbose_name='Жанры')
	world_premiere = models.DateField('Премьера в мире', default=date.today )
	budget = models.PositiveIntegerField('Бюджет', default=0, help_text='сумма в долларах' )
	fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0, help_text='сумма в долларах' )
	fees_in_world  = models.PositiveIntegerField('Сборы в мире', default=0, help_text='сумма в долларах' )
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
	url = models.SlugField(max_length=100, unique=True)
	draft = models.BooleanField('Черновик', default=False)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'

class MovieShots(models.Model):
	'''Shortcuts from movie'''
	title = models.CharField('Название', max_length=150)
	description = models.TextField('Описание', max_length =3000)
	image = models.ImageField('Shortcuts', upload_to='movie_shots/')
	movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Кадр из фильма'
		verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
	'''Stars of rating'''
	value = models.PositiveSmallIntegerField('Значение ретинга', default= 0)

	def __str__(self):
		return self.value

	class Meta:
		verbose_name = 'Звезда рейтинга'
		verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
	'''Movie rating'''
	ip = models.CharField('IP adres', max_length=15)
	star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Star')
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')


	def __str__(self):
		return f'{self.star} - {self.movie}'

	class Meta:
		verbose_name = 'Ретинг'
		verbose_name_plural = 'Ретинги'


class Reviews(models.Model):
	'''Reviews'''
	email = models.EmailField()
	name = models.CharField('Имя', max_length=100)
	text = models.TextField('Отзыв', max_length=4000)
	parent = models.ForeignKey('self', verbose_name= 'Родитель', on_delete=models.SET_NULL, blank=True, null=True)
	movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name} - {self.movie}'

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'



