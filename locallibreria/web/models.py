from django.db import models
from django.urls import reverse
import uuid


class Preparacion(models.Model):
    #Model representing a book genre."""
	tipo_prep = models.CharField(max_length=200)
	
	def __str__(self):
		return self.tipo_prep



class Receta(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	titulo = models.CharField(max_length=100)
	receta = models.TextField(max_length=3000)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
	preparacion = models.ManyToManyField(Preparacion)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('RECETA-', args=[str(self.id)])	
		

class Autor(models.Model):
	
	pnombre = models.CharField(max_length=100)
	papellido = models.CharField(max_length=100)

	class Meta:
		ordering = ['papellido', 'pnombre']


	def get_absolute_url(self):
		return reverse('detalles-autor', args=[str(self.id)])

	def __str__(self):
		return f'{self.papellido}, {self.pnombre}'		

