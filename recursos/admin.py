from django.contrib import admin
from .models import Recurso, Video, Articulo



class RecursoAdmin(admin.ModelAdmin):
    list_display = ['title','tipo','get_absolute_url']

admin.site.register(Recurso, RecursoAdmin)

# admin.site.register(Recurso)
admin.site.register(Video)
admin.site.register(Articulo)