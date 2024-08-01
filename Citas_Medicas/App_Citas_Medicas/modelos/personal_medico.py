from django.db import models
from .usuario import Usuario

# Definición de la clase PersonalMedico que hereda de models.Model
class PersonalMedico(models.Model):
    # Campo que crea una relación uno a uno con el modelo Usuario
    # on_delete=models.CASCADE indica que si se elimina un Usuario, se elimina el PersonalMedico asociado
    # related_name='medico' permite acceder al personal médico desde el modelo Usuario con usuario.medico
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='medico')
    
    # Campo de texto que almacena la especialidad del personal médico, con un máximo de 100 caracteres
    especialidad = models.CharField(max_length=100)

    # Método que define la representación en cadena del objeto PersonalMedico
    def __str__(self):
        # Retorna el nombre completo del usuario asociado al personal médico
        return self.usuario.nombre_completo
