from django.contrib import admin
from film.models import *
# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'film_genre')
    list_display_links = ('name', 'film_genre')

