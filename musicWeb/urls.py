"""musicWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog.views import  albums, index, artist, countries, AlbumDetailView, ArtistDetailView,CountryDetailView, genres,GenresDetailView,SearchResultsListView,songs
from catalog.views import  CreateSong, CreateAlbum, CreateArtist
from catalog.views import  DeleteSong, DeleteAlbum, DeleteArtist
from catalog.views import   ModifySong, ModifyAlbum, ModifyArtist
from django.conf import settings # new
from django.urls import path # new
from django.conf.urls.static import static # new
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #login
    path('accounts/', include('django.contrib.auth.urls')),
    #Index
    path('', index, name='index'),
    #Songs
    path('song/', songs, name='song'),
    #Artist
    path('artist/', artist, name='artist'),
    path('artist/details/<int:pk>', ArtistDetailView.as_view(), name='artistDetail'),
    #Album
    path('album/details/<int:pk>', AlbumDetailView.as_view(), name='albumDetail'),
    path('album/', albums, name='album'),
    #Country
    path('countries/', countries, name='countries'),
    path('country/details/<int:pk>', CountryDetailView.as_view(), name='countryDetail'),
    #Genre
    path('genres/', genres, name='genres'),
    path('genres/details/<int:pk>', GenresDetailView.as_view(), name='genreDetail'),
    #Busqueda
    path('searchSongs/', SearchResultsListView.as_view(), name ='search_results'),

    #creacion de elementos
    path('song/create', CreateSong.as_view(), name='create_song'),
    path('album/create', CreateAlbum.as_view(), name='create_album'),
    path('artist/create', CreateArtist.as_view(), name='create_artist'),

    #EliminarRegistros
    path('song/delete/<int:pk>', DeleteSong.as_view(), name='delete_song'),
    path('artist/delete/<int:pk>', DeleteArtist.as_view(), name='delete_artist'),
    path('album/delete/<int:pk>', DeleteAlbum.as_view(), name='delete_album'),

    #Modificar Registros
    path('song/modify/<int:pk>',  ModifySong.as_view(), name='modify_song'),
    path('artist/modify/<int:pk>',  ModifyArtist.as_view(), name='modify_artist'),
    path('album/modify/<int:pk>',  ModifyAlbum.as_view(), name='modify_album'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)