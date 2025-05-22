from django.db import models

# Create your models here.
class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='lugares/', null=True, blank=True)

    def _str_(self):
        return self.nombre