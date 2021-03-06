from django.contrib import admin
from Empleados.models import Empleado,Falta_Atraso,Felicitaciones

class AdminEmpleado(admin.ModelAdmin):
    list_filter = ["rut"]
    search_fields = ["rut"]
    class Meta:
        model = Empleado
# Register your models here.


class AdminFalta_Atraso(admin.ModelAdmin):
    list_filter = ["empleado"]
    search_fields = ["empleado"]
    class Meta:
        model = Falta_Atraso


class AdminFelicitaciones(admin.ModelAdmin):
    list_filter = ["empleado"]
    search_fields = ["empleado"]
    class Meta:
        model = Felicitaciones


admin.site.register(Empleado,AdminEmpleado)
admin.site.register(Falta_Atraso, AdminFalta_Atraso)
admin.site.register(Felicitaciones, AdminFelicitaciones)

admin.site.site_header = 'Direccion de seguridad ciudadana, Inspección y Emergencia Comunal'