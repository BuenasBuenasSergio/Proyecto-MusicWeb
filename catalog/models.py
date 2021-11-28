from os import truncate
from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField, DateField, IntegerField, TextField
# Create your models here.



class Countries(models.Model):
    """Modelo de paises"""
    country  = CharField("Pais", max_length=50)
    image = models.ImageField("Imagen",upload_to='images/Countries', null=True, blank=True)

    def __str__(self):
        return self.country

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):      
        return reverse('countryDetail', args=self.id)

class Genre(models.Model):
    """Modelo de estilos musicales"""
    genre = CharField("genero Musical", max_length= 50)
    image = models.ImageField("Imagen" ,upload_to='images/Genre', null=True, blank=True)

    def __str__(self):
        return self.genre

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):      
        return reverse('genreDetail', args=self.id)
        
class Artist(models.Model):
    """Modelo para los artistas/Bandas"""

    name = CharField("Nombre Grupo/Cantante", max_length=80)
    debutYear = DateField("Año de debut")
    biography = TextField("Biografia")
    genre = models.ManyToManyField(Genre, blank=True)
    image = models.ImageField("Imagen",upload_to='images/Artist', null=True, blank=True)
    imageB = models.ImageField("Imagen Banner" ,upload_to='images/Artist/Banner', null=True, blank=True)
    country = models.ForeignKey( Countries, on_delete=models.SET_NULL, null=True, blank=True)
    


    def show_genre(self):
        '''Muestra genero para admin'''

        return ', '.join([gen.genre for gen in self.genre.all()[:3]])

    show_genre.short_description = 'Generos'


    @property
    def get_image_url(self):
        """Recibiendo URLS de Imagenes"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    
    @property
    def get_imageBanner_url(self):
        if self.imageB and hasattr(self.imageB, 'url'):
            return self.imageB.url


    def get_absolute_url(self):
        """Preparando para recibir el id en vistas"""
        return reverse('artistDetail', args=self.id)

    def __str__(self) :
        return self.name

class Album(models.Model):
    """Modelo de Album"""

    title = CharField("Titulo Album", max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True) 
    releaseDate = DateField("Año de debut")
    image = models.ImageField("Imagen",upload_to='images/Album', null=True, blank=True)
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def get_absolute_url(self):      
        return reverse('albumDetail', args=self.id)


    def __str__(self) :
        return self.title

class Songs(models.Model):

    """Modelo Para Canciones"""

    title = CharField("Titulo",max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, related_name='Artist')
    collab_artists = models.ManyToManyField(Artist, related_name='Collab', blank=True)
    album =  models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    release_date = DateField("Fecha de lanzamiento")
    views = IntegerField("Visitas", blank=True, null=True, default=0)
    genre = models.ManyToManyField(Genre, blank=True)
    audio = models.FileField(upload_to='Songs/', null=True, blank=True)

    def __str__(self) :
        return self.title
    

    def show_collab(self):
        '''Muestra genero para admin'''

        return ', '.join([coll.name for coll in self.collab_artists.all()[:3]])

    show_collab.short_description = 'Artista Colaborador'


    def show_genre(self):
        '''Muestra genero para admin'''

        return ', '.join([gen.genre for gen in self.genre.all()[:3]])

    show_genre.short_description = 'Generos'


    @property
    def get_song_url(self):
        """Recibiendo la URL de las canciones"""
        if self.audio and hasattr(self.audio, 'url'):
            return self.audio.url

    def get_field_values(self):
        return [field.value_to_string(self) for field in Songs._meta.fields]

    class Meta:
        verbose_name='Song'
        verbose_name_plural='Songs'