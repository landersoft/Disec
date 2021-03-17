from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from Empleados.models import Empleado,Falta_Atraso,Felicitaciones 

# Create your views here.
@login_required
def lista(request):
    return render(request, 'lista.html')

class ListaView(generic.ListView):
    model = Empleado
    #template_name = ''


class EmpleadoDetailView(generic.DetailView):
    queryset = Falta_Atraso.objects.all()
    template_name = "Empleados/empleado_detail.html"

            

