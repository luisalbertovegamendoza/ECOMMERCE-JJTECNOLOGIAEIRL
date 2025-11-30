from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
#from django.urls import reverse_lazy
from django.views.generic import (TemplateView , DetailView,ListView , CreateView , UpdateView , DeleteView)
#from .models import Producto
from .models import Producto



class PruebaListView(ListView):
    template_name= 'camara/index.html'
    model=Producto
    context_object_name = 'lista'  

class ProductoDetailView(DetailView):
    model=Producto  # Modelo que usará
    template_name='camara/producto_detalle.html' # Plantilla a renderizar
    context_object_name='producto' #  Nombre de la variable en la plantilla

