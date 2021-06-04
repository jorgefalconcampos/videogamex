import os 
from django.db import models as m
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save 
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



game_status = (
    (0, 'En stock'),
    (1, 'Sin stock'),
    (2, 'Archivado'),
    (3, 'Descontinuado')
)




# Modelo StaffPerson, representa al "personal" o miembro del staff y tiene accesos al dashboard

class StaffPerson(m.Model):
    name = m.OneToOneField(User, on_delete=m.CASCADE, related_name='staff')
    slug = m.SlugField(unique=True, null=True, blank=True)
    title = m.CharField(max_length=100, blank=True)
    email = m.EmailField(unique=True, null=True)
    image = m.ImageField(upload_to='staff/img/', default='staff/default-img.png')
    bio = m.TextField(max_length=500)
    facebook_URL = m.URLField(null=True, blank=True)
    twitter_URL = m.URLField(null=True, blank=True)
    linkedin_URL = m.URLField(null=True, blank=True)
    activated_account = m.BooleanField(default=False)

    def __str__(self):
        return self.name.username

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            StaffPerson.objects.create(name=instance)
        if not User.is_superuser:
            instance.StaffPerson.save()

    def image_filename(self):
        return os.path.basename(self.image.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.first_name+' '+self.name.last_name)
        super (StaffPerson, self).save(*args, **kwargs)

    def activate_account(self, *args, **kwargs):
        self.activated_account = True
        super (StaffPerson, self).save(*args, **kwargs)





# Modelo Category, representa una "categoría", tema o género de videojuego
class Category(m.Model):
    name = m.CharField(max_length=100)
    description = m.CharField(max_length=300)
    slug = m.SlugField(unique=True)
    image = m.ImageField(upload_to='categories/', default='categories/no-category.png')

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super (Category, self).save(*args, **kwargs)
   


# Modelo Game, representa una juego
class Game(m.Model):
    author = m.ForeignKey(StaffPerson, on_delete=m.CASCADE, related_name='author')
    title = m.CharField(max_length=350)
    slug = m.SlugField(unique=True)
    category = m.ForeignKey(Category, on_delete=m.CASCADE, related_name='catego', default='1')
    image = m.ImageField(upload_to='img/', default='games/covers/no-img.jpg')
    released_date = m.DateTimeField(blank=True, null=True) # fecha en la que se lanzó el videojuego al mercado
    published_date = m.DateTimeField(blank=True, null=True) # fecha en la que videogamex subió el juego a la plataforma, control interno
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


# Modelo Comment, representa un "comentario" dentro de un post
class Comment(m.Model):
    in_game = m.ForeignKey(Game, on_delete=m.CASCADE, related_name="comments")
    author = m.CharField(max_length=125)
    author_email = m.EmailField()
    comment_body = m.TextField()
    created_date = m.DateTimeField(auto_now_add=True)
    is_approved = m.BooleanField(default=False)
    has_report = m.BooleanField(default=False)

    # approve method, to approve or disapprove comments
    def approve(self):
        self.is_approved = True
        self.save()

    def report(self):
        self.has_report = True
        self.save()

    def approved_comments(self):
        return self.Comment.objects.filter(is_approved=True)




