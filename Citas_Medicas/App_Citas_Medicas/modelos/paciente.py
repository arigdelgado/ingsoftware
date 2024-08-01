from django.db import models
from .usuario import Usuario

# Definición de la clase Paciente que hereda de models.Model
class Paciente(models.Model):
    # Campo que crea una relación uno a uno con el modelo Usuario
    # on_delete=models.CASCADE indica que si se elimina un Usuario, se elimina el Paciente asociado
    # related_name='paciente' permite acceder al paciente desde el modelo Usuario con usuario.paciente
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='paciente')
    
    # Campo de texto que almacena la dirección del paciente con un máximo de 255 caracteres
    direccion = models.CharField(max_length=255)
    
    # Campo de texto que almacena el número de teléfono del paciente con un máximo de 20 caracteres
    telefono = models.CharField(max_length=20)
    
    # Campo de texto que almacena el historial médico del paciente
    historial_medico = models.TextField()

    # Método que define la representación en cadena del objeto Paciente
    def __str__(self):
        # Retorna el nombre completo del usuario asociado al paciente
        return self.usuario.nombre_completo
