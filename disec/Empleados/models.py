from django.db import models

# Create your models here.
class Empleado(models.Model):

    CONTRATA = 'contrata'
    INDEFINIDO = 'indefinido'
    HONORARIOS = 'honorarios'

    TIPO = [
        (CONTRATA, 'contrata'),
        (INDEFINIDO, 'indefinido'),
        (HONORARIOS, 'honorarios'),
    ]

    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    licencia_conducir = models.CharField(max_length=1)

    tipo_contrato = models.CharField(max_length=10, choices=TIPO)
    fecha_contrata = models.DateField(blank=True)
    vigencia = models.DateField(blank=True)
    contacto_emergencia = models.CharField(max_length=100)
    telefono_emergencia = models.CharField(max_length=9)
    grupo_sanguineo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.nombre)


class Falta_Atraso(models.Model):
    tipo = models.CharField(max_length=10)
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)

    class Meta:
        ordering = ['empleado']
        verbose_name = 'Falta y/o atraso'
        verbose_name_plural = 'Faltas y/o atrasos'

        def __str__(self):
            return str(self.id)

class Felicitaciones(models.Model):
    tipo = models.CharField(max_length=10)
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)

    class Meta:
        ordering = ['empleado']
        verbose_name = 'Felicitaciones y Distincion'
        verbose_name_plural = 'Felicitaciones y Distinciones'

        def __str__(self):
            return str(self.id)

    