from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


TIPOS = (('artículo', 'Artículo'), ('video', 'Video'))

class Recurso(models.Model):    
    tipo = models.CharField(max_length=20,default="recurso", choices=TIPOS, blank=True)
    title = models.CharField("Título", max_length=50)
    likes = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return f"{self.tipo}/{self.id}/"
    
    def __str__(self):
        return self.title
   
class Articulo(Recurso):
    category = models.CharField("Categoría", max_length=50)
    def save(self, *args, **kwargs):
                self.tipo = TIPOS[0][0]
                super(Articulo, self).save(*args, **kwargs)

class Video(Recurso):
    uri = models.URLField("URI Video", max_length=200)
    def save(self, *args, **kwargs):
                self.tipo = TIPOS[1][0]
                super(Video, self).save(*args, **kwargs)
   