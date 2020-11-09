from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Preparacion, Receta, Autor

# Create your views here.
def index(request):

    num_recetas=Receta.objects.all().count()
    num_autores=Autor.objects.count()

    return render(
        request,
        'index.html',
        context={'num_recetas':num_recetas, 'num_autores':num_autores},
    )

def novedades(request):
    return render(
        request, 
        'novedades.html',
)

def dulces(request):
    return render(
        request, 
        'dulces.html',
)

def saladas(request):
    return render(
        request, 
        'saladas.html',
)

def bebidas(request):
    return render(
        request, 
        'bebidas.html',
)

def pret(request):
    return render(
        request, 
        'pret.html',
)

def pie(request):
    return render(
        request, 
        'pie.html',
)

def capu(request):
    return render(
        request, 
        'capu.html',
)

class AutorCreate(CreateView):
    model = Autor
    fields = ['pnombre', 'papellido', 'fechanac', 'fechamuerte']

class AutorUpdate(UpdateView):
    model = Autor
    fields = ['pnombre', 'papellido', 'fechanac', 'fechamuerte']

class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('index')


from django.views import generic
class AutorDetailView(generic.DetailView):
    model = Autor