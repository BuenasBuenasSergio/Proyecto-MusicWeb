from django.contrib import admin
from .models import Songs, Artist, Album,Genre, Countries
# Register your models here.

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist','show_collab' ,'album','show_genre' ,'release_date', 'views', 'audio']
    list_filter = ['title', 'album','release_date', 'views']



@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'debutYear', 'show_genre','country' ,'biography', 'image']
    list_filter = ['name', 'debutYear']
    read_only = ['image']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'releaseDate', 'image']
    list_filter = ['title', 'releaseDate']
    read_only = ['image']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass



@admin.register(Countries)
class GenreAdmin(admin.ModelAdmin):
    pass