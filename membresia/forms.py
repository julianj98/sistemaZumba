from django import forms
from .models import Planes, Cliente

class PlanesForm(forms.ModelForm):
  
    class Meta:
        model= Planes
        fields= ('description',
                 'precio',
                 'Cantidad_Clases',
                 )

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields=('name',
                'last_name',
                'Tipo_plan',
                'fecha_inicio',
                'fecha_fin',
                'state',)