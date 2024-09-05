from django.db import models
from .usuario import Usuario

class PersonalAdministrativo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='administrativo')
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.nombre_completo
