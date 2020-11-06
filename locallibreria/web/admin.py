from django.contrib import admin

# Register your models here.

from . models import Preparacion, Receta, Autor

admin.site.register(Preparacion)
admin.site.register(Receta)
admin.site.register(Autor)