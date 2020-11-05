from django.db import models
from django.urls import reverse         #redirecciona una url de un libro al browser
import uuid                             #se utilzia para definir atributos clave (PK)

# Create your models here.
class bebida(models.Model):
    #Model representing a book genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name


