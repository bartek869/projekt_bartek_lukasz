from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

#Director – model przechowujący dane o reżyserach (imię i data urodzenia).

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

#Movie – model reprezentujący film, z tytułem, opisem, rokiem wydania i powiązaniem z reżyserem.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, related_name='genres')

    def __str__(self):
        return self.name

#Genre – model przechowujący gatunki filmów, powiązany wiele do wielu z modelami Movie.