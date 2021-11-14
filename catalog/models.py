from django.core.files.images import ImageFile
from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.db.models.fields.files import ImageFieldFile

# Create your models here.


class Artist(models.Model):
    """Modelo para los artistas/Bandas"""

    name = CharField("Nombre Grupo/Cantante", max_length=80)
    debutYear = DateField("Año de debut")
    biography = TextField("Biografia")
    image = ImageFile("Imagen")
    #country
    #label

    def __str__(self) :
        return self.name


class Album(models.Model):
    """Modelo de Album"""

    title = CharField("Titulo", max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, blank=True) 
    releaseDate = DateField("Año de debut")
    #image = ImageFile
    
    def __str__(self) :
        return self.title


class Songs(models.Model):

    """Modelo Para Canciones"""

    title = CharField("Titulo",max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    #collab_artists
    album =  models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    release_date = DateField("Fecha de lanzamiento")
    views = IntegerField("Visitas", blank=True)
    #genre =
    #language

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name='Song'
        verbose_name_plural='Songs'