from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_admin = models.BooleanField(default=False)  # True para administradores

    def __str__(self):
        return f"{self.user.username} - {'Admin' if self.es_admin else 'Usuario'}"