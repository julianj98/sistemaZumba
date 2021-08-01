from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                ListView,
                                DetailView,
                                CreateView,
                                DeleteView,
                                UpdateView)
from .models import Cliente, Planes
from  .forms import PlanesForm, ClientesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


# Create your views here.

class inicioView(LoginRequiredMixin, TemplateView):
    template_name = "inicio.html"


class pruebaView(LoginRequiredMixin,ListView):
    template_name = 'clientes_all.html'
    model = Cliente
    paginate_by = 6
    context_object_name = "Lista_clientes"
    ordering = '-last_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Cliente.objects.filter(
            dni__icontains=palabra_clave,

        )
        return lista


class adminClienteView(LoginRequiredMixin,ListView):
    template_name = 'clientes_admin.html'
    model = Cliente
    paginate_by = 6
    context_object_name = "Lista_clientes"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Cliente.objects.filter(
            dni__icontains=palabra_clave
        )
        return lista

class ClienteDetailView(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = "detail_cliente.html"


class successView(LoginRequiredMixin,TemplateView):
    template_name = "success.html"


class ClienteCreateView(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "add_cliente.html"
    form_class=ClientesForm
    #fields = ("__all__")
    success_url = reverse_lazy('clientes_app:clientes_all')
    
    def form_valid(self, form):
        # logica del proceso
        Cliente = form.save(commit=False)
        Cliente.clases = Cliente.Tipo_plan.Cantidad_Clases
        print(Cliente.clases)
        Cliente.save()
        return super(ClienteCreateView, self).form_valid(form)


class PlanesListView(LoginRequiredMixin,ListView):
    model = Planes
    template_name = "planes_all.html"


class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = "update_cliente.html"
    form_class=ClientesForm
    success_url = reverse_lazy('clientes_app:clientes_admin')
    
    def form_valid(self, form):
        # logica del proceso
        Cliente = form.save(commit=False)
        Cliente.clases = Cliente.Tipo_plan.Cantidad_Clases
        print(Cliente.clases)
        Cliente.save()
        return super(ClienteUpdateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "cliente_delete.html"
    success_url = reverse_lazy('clientes_app:clientes_admin')


class PlanesListView(LoginRequiredMixin,ListView):
    model = Planes
    template_name = "list_planes.html"
    context_object_name= "planes"


class ClientesPorPlanListView(LoginRequiredMixin,ListView):
    template_name = "list_by_plan.html"
    context_object_name="clientes"
    def get_queryset(self):
        # el codigo que yo quiera
        plan = self.kwargs['id']
        lista = Cliente.objects.filter(
            Tipo_plan_id=plan
        )
        return lista


class PlanesCreateView(LoginRequiredMixin,CreateView):
    form_class=PlanesForm
    template_name = "add_plan.html"
    success_url = reverse_lazy('clientes_app:planes_list')
    



class PlanesDeleteView(LoginRequiredMixin,DeleteView):
    model = Planes
    template_name = "plan_delete.html"
    success_url = reverse_lazy('clientes_app:planes_list')


class PlanesUpdateView(LoginRequiredMixin,UpdateView):
    model = Planes
    form_class=PlanesForm
    template_name = "update_plan.html"
    success_url = reverse_lazy('clientes_app:planes_list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # logica del proceso
        return super(PlanesUpdateView, self).form_valid(form)

def RegistrarClase(request,**kwargs):
    cliente_id = kwargs['id']
    clienteActual = Cliente.objects.get(pk=cliente_id)
    context={"nombre":clienteActual.name,
             "apellido": clienteActual.last_name,
             "Clases_actuales":clienteActual.clases,
             "estado":clienteActual.state,
             }
    if request.method == 'POST':
        #tipoPlan_id= clienteActual.Tipo_plan.id
        #tipoPlan
        clienteActual.clases= clienteActual.clases-1
        if clienteActual.clases == 0:
            clienteActual.state = False
        elif clienteActual.clases >0:
            clienteActual.state = True
        clienteActual.save()
        return redirect('clientes_app:clientes_all')
    return render(request ,'inicio.html',context)

def Vencimiento(request,**kwargs):
    cliente_id = kwargs['id']
    success_url = reverse_lazy('clientes_app:planes_list')
    clienteActual = Cliente.objects.get(pk=cliente_id)
    context={
             "Clases_actuales":clienteActual.clases,
             "fecha_fin":clienteActual.fecha_fin,
             "estado":clienteActual.state}
    if request.method == 'POST':
        now=datetime.now()
        if now.date>clienteActual.fecha_fin:
            clienteActual.clases=0
        clienteActual.save()
        return redirect('clientes_app:inicio')
    return render(request ,'inicio.html',context)


"""def EstadoCliente(request,**kwargs):
    cliente_id = kwargs['id']
    clienteActual = Cliente.objects.get(pk=cliente_id)
    context={"estado":clienteActual.state,
             }
    if request.method=='POST':
        if clienteActual.clases == 0:
            clienteActual.state = False
        clienteActual.save()
    return render(request ,'inicio.html',context)"""

"""class RegistrarClaseUpdateView(UpdateView):
    model = Cliente
    fields = [
        'name',
        'last_name',
        'Tipo_plan',
        'fecha_inicio',
        'fecha_fin',
        "state",
    ]
    template_name = "detail_cliente.html"
    success_url = reverse_lazy('clientes_app:clientes_all')
    
    def  get_clases(self):
        clases = self.Cliente.Tipo_plan.Cantidad_Clases - 1
        print(clases)
        return clases"""
    
"""class RegistrarClaseUpdateView(UpdateView):
    model = Cliente
    template_name = "detail_cliente.html"
    success_url = reverse_lazy('clientes_app:inicio')
    
    def form_valid(self, form):
        # logica del proceso
        Cliente = form.save(commit=False)
        Cliente.Tipo_plan.Cantidad_Clases = Cliente.Tipo_plan.Cantidad_Clases -1
        Cliente.save()
        return super(RegistrarClaseUpdateView, self).form_valid(form)"""