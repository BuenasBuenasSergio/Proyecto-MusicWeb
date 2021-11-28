from django.db.models.query_utils import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from catalog.models import Songs, Album, Artist, Countries, Genre
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# django.views.generic import ListView

# Create your views here.

#VISTA INDEX
def index(request):
        '''Pagina Inicial de nuestra Web'''
        songs = Songs.objects.all().order_by('-id')[:4]
        albums = Album.objects.all().order_by('-id')[:4]
        artist = Artist.objects.all().order_by('-id')[:4]

        #paginator = Paginator(songs, 12)
        #page_number = request.GET.get('page')
        #page_obj = paginator.get_page(page_number)

        datos = {'songs' : songs,
                'album' : albums,
                'artist' : artist}
        return render(request, 'index.html', context=datos)


#VISTAS Canciones
@login_required
def songs(request):
        """Pagina listado de artistas"""
        songs = Songs.objects.all().order_by('title')

        paginator = Paginator(songs, 12)
        page_number = request.GET.get('page')
        song_pag = paginator.get_page(page_number)

        datos = {'songs': song_pag}

        
        return render(request, 'songs.html', context=datos)

#VISTAS ARTISTAS
@login_required
def artist(request):
        """Pagina listado de artistas"""
        artistas = Artist.objects.all().order_by('name')

        paginator = Paginator(artistas, 12)
        page_number = request.GET.get('page')
        artist_pag = paginator.get_page(page_number)


        datos = {'artistas': artist_pag}

        
        return render(request, 'artist.html', context=datos)


class ArtistDetailView(DetailView,LoginRequiredMixin):

    model = Artist
    template_name = 'artistdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_list'] = Songs.objects.filter(Q(artist=self.object) | Q(collab_artists=self.object)).distinct().order_by('-views')[:5]
        context['album_list'] = Album.objects.filter(artist=self.object)
        return context

#VISTAS ALBUMS
@login_required
def albums(request):
        """Pagina listado de Paises"""
        albums = Album.objects.all().order_by('title')

        paginator = Paginator(albums, 12)
        page_number = request.GET.get('page')
        album_pag = paginator.get_page(page_number)

        datos = {'albums': album_pag}

        return render(request, 'album.html', context=datos)


class AlbumDetailView(DetailView, LoginRequiredMixin):
    """Detalles de un album"""
    model = Album
    template_name = 'albumdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_list'] = Songs.objects.filter(album=self.object)
        return context


#VISTAS PAISES
@login_required
def countries(request):
        """Pagina listado de Paises"""
        countries = Countries.objects.all()

        datos = {'countries': countries}

        return render(request, 'countries.html', context=datos)

class CountryDetailView(DetailView):
        """Cantates de cada pais"""
        model = Countries
        template_name = 'countrydetails.html'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['artist_list'] = Artist.objects.filter(country=self.object)
                return context


#VISTAS GENEROS
@login_required
def genres(request):
        """Pagina listado de Paises"""
        genres = Genre.objects.all()

        datos = {'genres': genres}

        return render(request, 'genres.html', context=datos)

class GenresDetailView(DetailView):
        """Cantantes perteneciente a al genero"""
        model = Genre
        template_name = 'genredetails.html'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['artist_list'] = Artist.objects.filter(genre=self.object)
                return context


class SearchResultsListView(ListView):
        """Busqueda de canciones"""
        model = Songs
        context_object_name = 'songs_list'
        template_name = 'search_songs.html'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                query = self.request.GET.get('q')
                context['songs_list'] = Songs.objects.filter(title__icontains=query).order_by('-id')[:4]
                context['album_list'] = Album.objects.filter(title__icontains=query).order_by('-id')[:4]
                context['artist_list'] = Artist.objects.filter(name__icontains=query).order_by('-id')[:4]
                return context


#Creacion de registros
class CreateSong(generic.CreateView):
        """Crear Cancion"""
        model = Songs
        fields = '__all__'
        template_name = 'create/createSong.html'
        
        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.album.id})


class CreateAlbum(generic.CreateView):
        """Crear Album"""
        model = Album
        fields = '__all__'
        template_name = 'create/createAlbum.html'
        success_url = '/album'


class CreateArtist(generic.CreateView):
        """Crear Artista"""
        model = Artist
        fields = '__all__'
        template_name = 'create/createArtist.html'
        success_url = '/artist'


#Eliminacion de Registros

class DeleteSong(generic.DeleteView):
        """Eliminar Cancion"""
        model = Songs
        template_name = 'delete/song_delete_confirm.html'

        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.album.id})


class DeleteAlbum(generic.DeleteView):
        """Eliminar Album"""
        model = Album
        template_name = 'delete/album_delete_confirm.html'

        def get_success_url(self):
                return reverse_lazy('artistDetail', kwargs={'pk': self.object.artist.id})


class DeleteArtist(generic.DeleteView):
        """Eliminar Artista"""
        model = Artist
        success_url = 'artist/'
        template_name = 'delete/artist_delete_confirm.html'


#Modificacion de registros

class ModifySong(generic.UpdateView):
        """Modificar Cancion"""
        model = Songs
        fields = '__all__'
        template_name = 'modify/modify_song.html'

        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.album.id})

class ModifyArtist(generic.UpdateView):
        """Modificar Artista"""
        model = Artist
        fields = '__all__'
        template_name = 'modify/modify_artist.html'

        def get_success_url(self):
                return reverse_lazy('artistDetail', kwargs={'pk': self.object.id})

class ModifyAlbum(generic.UpdateView, LoginRequiredMixin):
        """Modificar Album"""
        model = Album
        fields = '__all__'
        template_name = 'modify/modify_album.html'

        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.id})
