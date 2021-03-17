from . import views
#from ventas.views import nueva,index
from django.urls import path, include
from django.views import generic


urlpatterns = [
    path(r'',views.lista, name='lista'),
    path(r'lista',views.ListaView.as_view(), name='lista'),
    path(r'lista/pecados', views.EmpleadoDetailView.as_view())
]
