from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Songs, Album, Artist, Countries, Genre
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
# django.views.generic import ListView

# Create your views here.

def index(request):
        '''Pagina Inicial de nuestra Web'''
        songs = Songs.objects.all()
        albums = Album.objects.all()

        datos = {'songs' : songs,
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


class CreateSong(generic.CreateView):
        """Crear Cancion"""
        model = Songs
        fields = '__all__'
        template_name = 'createSong.html'
        success_url = '/'