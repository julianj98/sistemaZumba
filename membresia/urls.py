from django.contrib import admin
from django.urls import path
from . import views

app_name="clientes_app"
urlpatterns = [
    path('',views.inicioView.as_view(), name="inicio"),
    path('home/',views.pruebaView.as_view()),
    path('ver_cliente/<pk>',views.ClienteDetailView.as_view()),
    path('add_cliente',views.ClienteCreateView.as_view()),
    path('success', 
         views.successView.as_view(),
         name="correcto"),

]
