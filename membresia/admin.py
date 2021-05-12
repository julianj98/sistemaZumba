from django.contrib import admin
from .models import Cliente, Planes

# Register your models here.

class clienteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'Tipo_plan',
        'fecha_inicio',
        'fecha_fin',
        'state',
    )
    search_fields = ('name',)
    list_filter = ("state",'Tipo_plan',)

admin.site.register(Cliente,clienteAdmin)
admin.site.register(Planes)
