from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cliente

# Create your views here.

class pruebaView(TemplateView):
    template_name='home.html'
    model= Cliente
    context_object_name="Lista_clientes"
    