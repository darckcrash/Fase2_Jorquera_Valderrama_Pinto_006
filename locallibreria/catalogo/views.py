from django.shortcuts import render
from . models import bebida
from django.views import generic


# Create your views here.
def index(request):
    num_bebida = bebida.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_bebida': num_bebida},
    )
