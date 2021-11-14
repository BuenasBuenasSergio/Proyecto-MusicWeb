from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, IntegerField, TextField
# Create your models here.


class Artist(models.Model):
    """Modelo para los artistas/Bandas"""

    name = CharField("Nombre Grupo/Cantante", max_length=80)
    debutYear = DateField("Año de debut")
    biography = TextField("Biografia")
    image = models.ImageField(upload_to='images/Artist', null=True, blank=True)
    #country
    #label

    def __str__(self) :
        return self.name


class Album(models.Model):
    """Modelo de Album"""

    title = CharField("Titulo", max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True) 
    releaseDate = DateField("Año de debut")
    image = models.ImageField(upload_to='images/Album', null=True, blank=True)
    
    def __str__(self) :
        return self.title


class Songs(models.Model):

    """Modelo Para Canciones"""

    title = CharField("Titulo",max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='Artist')
    collab_artists = models.ManyToManyField(Artist, related_name='Collab', blank=True)
    album =  models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    release_date = DateField("Fecha de lanzamiento")
    views = IntegerField("Visitas", blank=True, null=True)
    #genre =
    #language
    audio = models.FileField(upload_to='Songs/', null=True, blank=True)

    def __str__(self) :
        return self.title
    

    def show_collab(self):
        '''Muestra genero para admin'''
        return ', '.join([coll.name for coll in self.collab_artists.all()[:3]])
    show_collab.short_description = 'Collab Artist'

    class Meta:
        verbose_name='Song'
        verbose_name_plural='Songs'