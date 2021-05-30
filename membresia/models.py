from django.db import models
from datetime import  date
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    clases= models.PositiveIntegerField(blank=True,null=True,verbose_name="Clases disponibles")
    #modelChoicefield
    fecha_inicio=models.DateField(auto_now=False, verbose_name="Fecha de inicio",default=date.today)
    fecha_fin=models.DateField(auto_now=False, verbose_name="Fecha de finalizacion")
    state=models.BooleanField(verbose_name='Activo',default=True) 
    
    class Meta:
        verbose_name= "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
""""
@receiver(post_save, sender=Cliente)
def cliente_post_save_receiver(sender,instance, **kwargs):
    cliente_id=instance.id
    tipo_plan=instance.Tipo_plan
    instance.clases = instance.Tipo_plan.Cantidad_Clases
    instance.save()
    print(tipo_plan)"""