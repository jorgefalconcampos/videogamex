from django.db import models as m
from django.db.models.signals import pre_save, post_save 
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



game_status = (
    (0, 'En stock'),
    (1, 'Sin stock'),
    (2, 'Archivado'),
    (3, 'Descontinuado')
)


# Modelo Category, representa una "categoría", tema o género de videojuego
class Category(m.Model):
    name = m.CharField(max_length=100)
    description = m.CharField(max_length=300)
    slug = m.SlugField(unique=True)
    image = m.ImageField(upload_to='categories/', default='no-category.png')

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super (Category, self).save(*args, **kwargs)
   


# Modelo Game, representa una juego
class Game(m.Model):
    title = m.CharField(max_length=150)
    slug = m.SlugField(unique=True)
    category = m.ForeignKey(Category, on_delete=m.CASCADE, related_name='catego', default='1')
    image = m.ImageField(upload_to='img/', default='no-img.png')
    published_date = m.DateTimeField(blank=True, null=True)
    status = m.IntegerField(choices=game_status, default=0)
    # Reacciones y votos para el post: fav, util, like o dislike
    vote_fav = m.IntegerField(default=0) 
    vote_util = m.IntegerField(default=0)     
    vote_tmbup = m.IntegerField(default=0) 
    vote_tmbdn = m.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super (Game, self).save(*args, **kwargs)





