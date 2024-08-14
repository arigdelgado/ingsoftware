from django.db import models
from .usuario import Usuario

class Administrador(models.Model):
    """
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.modelos.administrador import Administrador

    >>> # Crear un usuario
    >>> usuario = Usuario.objects.create(nombre_completo='Pepe', correo='pe.pe@example.com', tipo_usuario='Administrador')

    >>> # Crear un administrador asociado al usuario
    >>> administrador = Administrador.objects.create(usuario=usuario, permisos='admin, edit')

    >>> # Verificar que el administrador se creó correctamente
    >>> administrador.usuario.nombre_completo
    'Pepe'

    >>> # Verificar el método __str__
    >>> str(administrador)
    'Pepe'

    >>> # Verificar los permisos
    >>> administrador.permisos
    'admin, edit'
    """

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='administrador')
    permisos = models.TextField()

    def __str__(self):
        return self.usuario.nombre_completo
