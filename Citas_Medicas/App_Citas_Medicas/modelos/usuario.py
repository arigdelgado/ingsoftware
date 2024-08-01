from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=50)

     # Indica que el campo de autenticación es 'correo'
    USERNAME_FIELD = 'correo'
    # Campos que deben ser requeridos al crear un usuario, aparte de 'correo'
    REQUIRED_FIELDS = ['nombre_completo', 'tipo_usuario']

    objects = BaseUserManager()

    def __str__(self):
        return self.nombre_completo