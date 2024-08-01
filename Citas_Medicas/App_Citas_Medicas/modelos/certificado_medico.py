from django.db import models
from .paciente import Paciente
from .personal_medico import PersonalMedico
from .personal_administrativo import PersonalAdministrativo

# Definición de la clase CertificadoMedico que hereda de models.Model
class CertificadoMedico(models.Model):
    # Campo que almacena el ID de la consulta asociada
    idconsulta = models.IntegerField()
    
    # Campo que almacena la fecha y hora de emisión del certificado, asignada automáticamente al crear el objeto
    fecha_emision = models.DateTimeField(auto_now_add=True)
    
    # Campo que crea una relación de muchos a uno con el modelo Paciente
    # on_delete=models.CASCADE indica que si se elimina un Paciente, se eliminan los certificados asociados
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # Campo que crea una relación de muchos a uno con el modelo PersonalMedico
    # on_delete=models.CASCADE indica que si se elimina un PersonalMedico, se eliminan los certificados asociados
    medico = models.ForeignKey(PersonalMedico, on_delete=models.CASCADE)
    
    # Campo que crea una relación de muchos a uno con el modelo PersonalAdministrativo
    # on_delete=models.CASCADE indica que si se elimina un PersonalAdministrativo, se eliminan los certificados asociados
    administrativo = models.ForeignKey(PersonalAdministrativo, on_delete=models.CASCADE)

    # Método que define la representación en cadena del objeto CertificadoMedico
    def __str__(self):
        # Retorna una cadena que incluye el ID del certificado y la fecha de emisión
        return f"Certificado {self.id} - {self.fecha_emision}"
