from django.db import models

# Create your models here.
class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='lugares/', null=True, blank=True)

    def _str_(self):
        return self.nombre

class Hotel (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    sitio_web = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='hoteles/', null=True, blank=True)

    def _str_(self):
        return self.nombre