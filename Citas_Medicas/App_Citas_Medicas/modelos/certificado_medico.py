from django.db import models
from .paciente import Paciente
from .personal_medico import PersonalMedico
from .personal_administrativo import PersonalAdministrativo

class CertificadoMedico(models.Model):
    idconsulta = models.IntegerField()  # ID de la consulta asociada
    fecha_emision = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(PersonalMedico, on_delete=models.CASCADE)
    administrativo = models.ForeignKey(PersonalAdministrativo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Certificado {self.id} - {self.fecha_emision}"
