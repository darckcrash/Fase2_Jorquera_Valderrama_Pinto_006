from django.db import models
from django.urls import reverse
import uuid


class Preparacion(models.Model):
    #Model representing a book genre."""
	tipo_prep = models.CharField(max_length=200)
	
	def __str__(self):
		return self.tipo_prep



class Receta(models.Model):

	titulo = models.CharField(max_length=100)
	receta = models.TextField(max_length=3000)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
	preparacion = models.ManyToManyField(Preparacion)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('receta-detail', args=[str(self.id)])	
		

class Autor(models.Model):
	
	pnombre = models.CharField(max_length=100)
	papellido = models.CharField(max_length=100)
	fechanac = models.DateField(null=True, blank=True)
	fechamuerte = models.DateField('Muerto', null=True, blank=True)

	class Meta:
		ordering = ['papellido', 'pnombre']


	def get_absolute_url(self):
		return reverse('autor-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.papellido}, {self.pnombre}'		

