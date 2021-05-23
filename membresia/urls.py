from django.contrib import admin
from django.urls import path
from . import views

app_name="clientes_app"
urlpatterns = [
    path('',views.inicioView.as_view(), name="inicio"),
    path('clientes_all/',views.pruebaView.as_view(),name="clientes_all"),
    path('ver_cliente/<pk>',views.ClienteDetailView.as_view(),name="cliente_detail"),
    path('add_cliente',views.ClienteCreateView.as_view()),
    path('success', 
         views.successView.as_view(),
         name="correcto"),

]
