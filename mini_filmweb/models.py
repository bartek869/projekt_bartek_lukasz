from django.db import models

# Model przechowujący dane o reżyserach
class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię i nazwisko")
    birth_date = models.DateField(verbose_name="Data urodzenia")

    def __str__(self):
        return self.name

# Model przechowujący dane o filmach
class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    release_year = models.PositiveIntegerField(verbose_name="Rok wydania")  # Użyłem PositiveIntegerField, aby uniknąć ujemnych lat
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', verbose_name="Reżyser")
    genres = models.ManyToManyField('Genre', related_name='movies', verbose_name="Gatunki", blank=True)  # Dodano blank=True

    def __str__(self):
        return self.title

# Model przechowujący gatunki filmów
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Gatunek")  # Dodano unique=True

    def __str__(self):
        return self.name
