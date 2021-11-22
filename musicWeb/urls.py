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
from catalog.views import  index, artist, countries, AlbumDetailView, ArtistDetailView, CountryDetailView
from django.conf import settings # new
from django.urls import path # new
from django.conf.urls.static import static # new


urlpatterns = [
    path('admin/', admin.site.urls),
    #Index
    #path('', HomePageView.as_view(), name='index'),
    path('', index, name='index'),
    #Artist
    path('artist/', artist, name='artist'),
    path('artist/details/<int:pk>', ArtistDetailView.as_view(), name='artistDetail'),
    #Album
    path('album/details/<int:pk>', AlbumDetailView.as_view(), name='albumDetail'),
    #Country
    path('countries/', countries, name='countries'),
    path('country/details/<int:pk>', CountryDetailView.as_view(), name='countryDetail'),
    #Genre
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)