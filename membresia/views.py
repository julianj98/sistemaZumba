from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                ListView,
                                DetailView,
                                CreateView,
                                DeleteView,
                                UpdateView)
from .models import Cliente, Planes

# Create your views here.


class inicioView(TemplateView):
    template_name = "inicio.html"


class pruebaView(ListView):
    template_name = 'clientes_all.html'
    model = Cliente
    paginate_by = 6
    context_object_name = "Lista_clientes"
    ordering = '-last_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Cliente.objects.filter(
            name__icontains=palabra_clave
        )
        return lista


class adminClienteView(ListView):
    template_name = 'clientes_admin.html'
    model = Cliente
    paginate_by = 6
    context_object_name = "Lista_clientes"

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
    fields = ("__all__")
    success_url = reverse_lazy('clientes_app:inicio')


class PlanesListView(ListView):
    model = Planes
    template_name = "planes_all.html"


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "update_cliente.html"
    fields = [
        'name',
        'last_name',
        'Tipo_plan',
        'fecha_inicio',
        'fecha_fin',
        "state",
    ]
    success_url = reverse_lazy('clientes_app:clientes_admin')

    def post(self, request, *args, **kwargs):
        print('*************************')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # logica del proceso
        return super(ClienteUpdateView, self).form_valid(form)


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "cliente_delete.html"
    success_url = reverse_lazy('clientes_app:clientes_admin')


class PlanesListView(ListView):
    model = Planes
    template_name = "list_planes.html"
    context_object_name= "planes"
    

class ClientesPorPlanListView(ListView):
    template_name = "list_by_plan.html"
    context_object_name="clientes"
    def get_queryset(self):
        # el codigo que yo quiera
        plan = self.kwargs['id']
        lista = Cliente.objects.filter(
            Tipo_plan_id=plan
        )
        return lista
