from django.contrib import admin
from .models import Songs, Artist, Album
# Register your models here.

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'release_date', 'views']
    list_filter = ['title', 'album','release_date', 'views']



@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'debutYear', 'biography', 'image']
    list_filter = ['name', 'debutYear']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass