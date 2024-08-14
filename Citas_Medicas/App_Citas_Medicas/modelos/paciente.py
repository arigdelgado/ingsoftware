from django.db import models
from .usuario import Usuario

class Paciente(models.Model):
    """
    >>> from django.contrib.auth.models import User
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.modelos.paciente import Paciente

    >>> # Crear un usuario
    >>> user = User.objects.create_user(username='ariana', password='secret')
    >>> usuario = Usuario.objects.create(id=user.id, nombre_completo='ariana', correo='ariana@gmail.com', tipo_usuario='Paciente')

    >>> # Crear un paciente
    >>> paciente = Paciente.objects.create(usuario=usuario, direccion='Calle 123', telefono='0987654321', historial_medico='Ninguno')

    >>> # Representación del paciente
    >>> str(paciente)
    'ariana'
    """

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='paciente')
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    historial_medico = models.TextField()

    def __str__(self):
        return self.usuario.nombre_completo