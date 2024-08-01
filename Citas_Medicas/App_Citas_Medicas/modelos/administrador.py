from django.db import models
from .usuario import Usuario

# Definición de la clase Administrador que hereda de models.Model
class Administrador(models.Model):
    # Campo que crea una relación uno a uno con el modelo Usuario
    # on_delete=models.CASCADE indica que si se elimina un Usuario, se elimina el Administrador asociado
    # related_name='administrador' permite acceder al administrador desde el modelo Usuario con usuario.administrador
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='administrador')
    
    # Campo de texto que almacena los permisos del administrador
    permisos = models.TextField()

    # Método que define la representación en cadena del objeto Administrador
    def __str__(self):
        # Retorna el nombre completo del usuario asociado al administrador
        return self.usuario.nombre_completo
