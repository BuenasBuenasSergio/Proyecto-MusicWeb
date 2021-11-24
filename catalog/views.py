from django.db.models.query_utils import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse
from catalog.models import Songs, Album, Artist, Countries, Genre
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
# django.views.generic import ListView

# Create your views here.

def index(request):
        '''Pagina Inicial de nuestra Web'''
        songs = Songs.objects.all().order_by('-id')
        albums = Album.objects.all()

        paginator = Paginator(songs, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        datos = {'songs' : page_obj,
                'album' : albums}
        return render(request, 'index.html', context=datos)



def artist(request):
        """Pagina listado de artistas"""
        artistas = Artist.objects.all()

        datos = {'artistas': artistas}

        return render(request, 'artist.html', context=datos)


def artistDetail(request, pk):

        details = get_object_or_404(Artist, pk=int(id))
        datos = {'details': details}

        return render(request, 'artistdetails.html', context=datos)


class ArtistDetailView(DetailView):

    model = Artist
    template_name = 'artistdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_list'] = Songs.objects.filter(Q(artist=self.object) | Q(collab_artists=self.object)).distinct().order_by('-views')[:5]
        context['album_list'] = Album.objects.filter(artist=self.object)
        return context

def albums(request):
        """Pagina listado de Paises"""
        albums = Album.objects.all().order_by('title')

        datos = {'albums': albums}

        return render(request, 'album.html', context=datos)


class AlbumDetailView(DetailView):

    model = Album
    template_name = 'albumdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_list'] = Songs.objects.filter(album=self.object)
        return context



def countries(request):
        """Pagina listado de Paises"""
        countries = Countries.objects.all()

        datos = {'countries': countries}

        return render(request, 'countries.html', context=datos)

class CountryDetailView(DetailView):

        model = Countries
        template_name = 'countrydetails.html'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['artist_list'] = Artist.objects.filter(country=self.object)
                return context


def genres(request):
        """Pagina listado de Paises"""
        genres = Genre.objects.all()

        datos = {'genres': genres}

        return render(request, 'genres.html', context=datos)

class GenresDetailView(DetailView):

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
        def get_queryset(self): # new
                query = self.request.GET.get('q')
                return Songs.objects.filter(title__icontains=query)



#Creacion de registros
class CreateSong(generic.CreateView):
        """Crear Cancion"""
        model = Songs
        fields = '__all__'
        template_name = 'create/createSong.html'
        success_url = '/'


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
        model = Songs
        
        template_name = 'delete/song_delete_confirm.html'

        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.album.id})


class DeleteAlbum(generic.DeleteView):
        model = Album
        template_name = 'delete/album_delete_confirm.html'

        def get_success_url(self):
                return reverse_lazy('artistDetail', kwargs={'pk': self.object.artist.id})


class DeleteArtist(generic.DeleteView):
        model = Artist
        success_url = 'artist/'
        template_name = 'delete/artist_delete_confirm.html'


#Modificacion de registros

class ModifySong(generic.UpdateView):
        model = Songs
        fields = '__all__'
        template_name = 'modify/modify_song.html'

        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.album.id})

class ModifyArtist(generic.UpdateView):
        model = Artist
        fields = '__all__'
        template_name = 'modify/modify_artist.html'

        def get_success_url(self):
                return reverse_lazy('artistDetail', kwargs={'pk': self.object.id})

class ModifyAlbum(generic.UpdateView):
        model = Album
        fields = '__all__'
        template_name = 'modify/modify_album.html'

        def get_success_url(self):
                return reverse_lazy('albumDetail', kwargs={'pk': self.object.id})
