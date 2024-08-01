from django.db import models
from .usuario import Usuario

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='paciente')
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    historial_medico = models.TextField()

    def __str__(self):
        return self.usuario.nombre_completo
