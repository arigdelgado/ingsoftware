from django.db import models
from .usuario import Usuario

class PersonalMedico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='medico')
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.nombre_completo
