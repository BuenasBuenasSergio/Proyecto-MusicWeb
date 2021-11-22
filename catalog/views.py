from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Songs, Album, Artist, Countries
from django.views.generic.detail import DetailView
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
        context['song_list'] = Songs.objects.all().filter()
        context['album_list'] = Album.objects.all().filter()
        return context


class AlbumDetailView(DetailView):

    model = Album
    template_name = 'albumdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['song_list'] = Songs.objects.all().filter()
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
        context['artist_list'] = Artist.objects.all().filter()
        return context



# class HomePageView(ListView):
#     model = Album
#     template_name = 'index.html'