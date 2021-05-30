from django.contrib import admin
from django.urls import path
from . import views

app_name="clientes_app"
urlpatterns = [
    path('',views.inicioView.as_view(), name="inicio"),
    path('clientes_all/',views.pruebaView.as_view(),name="clientes_all"),
    path('clientes_admin/',views.adminClienteView.as_view(),name="clientes_admin"),
    path('ver_cliente/<pk>',views.ClienteDetailView.as_view(),name="cliente_detail"),
    path('add_cliente',views.ClienteCreateView.as_view(),name="add_cliente"),
    path('success', 
         views.successView.as_view(),
         name="correcto"),
    path('delete_cliente/<pk>', 
         views.ClienteDeleteView.as_view(),
         name="delete_cliente"),
    path('update_cliente/<pk>', 
         views.ClienteUpdateView.as_view(),
         name="update_cliente"),
    path('planes_list', 
         views.PlanesListView.as_view(),
         name="planes_list"),
    path('clientes_by_plan/<id>', 
         views.ClientesPorPlanListView.as_view(),
         name="clientes_by_plan"),
    path('add_plan', 
         views.PlanesCreateView.as_view(),
         name="add_plan"),
    path('delete_plan/<pk>', 
         views.PlanesDeleteView.as_view(),
         name="delete_plan"),
    path('update_plan/<pk>', 
         views.PlanesUpdateView.as_view(),
         name="update_plan"),
    path('restar_clase/<int:id>', 
         views.RegistrarClase,
         name="restar_clase"),

]
