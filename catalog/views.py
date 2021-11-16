from django.shortcuts import render
from catalog.models import Songs, Album
# django.views.generic import ListView

# Create your views here.

def index(request):
        '''Pagina Inicial de nuestra Web'''
        songs = Songs.objects.all()
        albums = Album.objects.all()

        datos = {'songs' : songs,
                'album' : albums}

        return render(request, 'index.html', context=datos)



# class HomePageView(ListView):
#     model = Album
#     template_name = 'index.html'