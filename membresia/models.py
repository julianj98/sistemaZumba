from django.db import models

# Create your models here.
class Planes(models.Model):
    description = models.CharField('Descripción', max_length=70)
    precio= models.PositiveIntegerField('Precio')
    Cantidad_Clases= models.IntegerField('Cantidad de clases')
    
    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Cantidad de planes"
        ordering = ['description']
    
    def __str__(self):
        return  self.description 

class Cliente(models.Model):
    name= models.CharField(max_length=60,verbose_name="Nombre")
    last_name= models.CharField(max_length=60,verbose_name="Apellido")
    Tipo_plan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    #modelChoicefield
    fecha_inicio=models.DateField(auto_now=False, verbose_name="Fecha de inicio")
    fecha_fin=models.DateField(auto_now=False, verbose_name="Fecha de finalizacion")
    state=models.BooleanField('Activo',default=True) 
    
    class Meta:
        verbose_name= "Cliente"
    verbose_name_plural = "Clientes"
    ordering = ["-created"]
        
    def __str__(self):
        return self.name

