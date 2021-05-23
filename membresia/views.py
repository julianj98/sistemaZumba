from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Cliente

# Create your views here.

class inicioView(TemplateView):
    template_name = "inicio.html"


class pruebaView(ListView):
    template_name='clientes_all.html'
    model= Cliente
    paginate_by = 6
    context_object_name="Lista_clientes"
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Cliente.objects.filter(
        name__icontains=palabra_clave
    )
        return lista


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "detail_cliente.html"

class successView(TemplateView):
    template_name = "success.html"

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "add_cliente.html"
    fields=("__all__")
    success_url = reverse_lazy('clientes_app:correcto')
