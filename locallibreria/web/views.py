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
class RecetaCreate(CreateView):
    model = Receta
    fields = ['titulo', 'receta', 'autor', 'preparacion']

class RecetaUpdate(UpdateView):
    model = Receta
    fields = ['titulo', 'receta', 'autor', 'preparacion']

class RecetaDelete(DeleteView):
    model = Receta
    success_url = reverse_lazy('recetas')


from django.views import generic
class RecetaDetailView(generic.DetailView):
    model = Receta    
