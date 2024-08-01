from django.db import models
from .usuario import Usuario

# Definición de la clase PersonalAdministrativo que hereda de models.Model
class PersonalAdministrativo(models.Model):
    # Campo que crea una relación uno a uno con el modelo Usuario
    # on_delete=models.CASCADE indica que si se elimina un Usuario, se elimina el PersonalAdministrativo asociado
    # related_name='administrativo' permite acceder al personal administrativo desde el modelo Usuario con usuario.administrativo
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='administrativo')
    
    # Campo de texto que almacena el nombre del departamento al que pertenece el personal administrativo, con un máximo de 100 caracteres
    departamento = models.CharField(max_length=100)

    # Método que define la representación en cadena del objeto PersonalAdministrativo
    def __str__(self):
        # Retorna el nombre completo del usuario asociado al personal administrativo
        return self.usuario.nombre_completo
