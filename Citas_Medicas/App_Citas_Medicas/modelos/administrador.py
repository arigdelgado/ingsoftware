from django.db import models
from .usuario import Usuario

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='administrador')
    permisos = models.TextField()

    def __str__(self):
        return self.usuario.nombre_completo