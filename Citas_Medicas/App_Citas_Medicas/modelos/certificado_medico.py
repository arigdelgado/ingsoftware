from django.db import models
from .paciente import Paciente
from .personal_medico import PersonalMedico
from .personal_administrativo import PersonalAdministrativo

class CertificadoMedico(models.Model):
    """
    >>> from django.utils import timezone
    >>> from App_Citas_Medicas.modelos.paciente import Paciente
    >>> from App_Citas_Medicas.modelos.personal_medico import PersonalMedico
    >>> from App_Citas_Medicas.modelos.personal_administrativo import PersonalAdministrativo
    >>> from App_Citas_Medicas.modelos.certificado_medico import CertificadoMedico
    >>> from App_Citas_Medicas.modelos.usuario import Usuario

    >>> # Crear Usuarios
    >>> usuario_paciente = Usuario.objects.create(nombre_completo='paciente', correo='paciente@gmail.com', tipo_usuario='Paciente')
    >>> usuario_medico = Usuario.objects.create(nombre_completo='medico', correo='medico@gmail.com', tipo_usuario='Medico')
    >>> usuario_administrativo = Usuario.objects.create(nombre_completo='admin', correo='admin@gmail.com', tipo_usuario='Administrativo')

    >>> # Crear Paciente, PersonalMedico y PersonalAdministrativo
    >>> paciente = Paciente.objects.create(usuario=usuario_paciente, direccion='Calle 123', telefono='0915874236', historial_medico='Regular')
    >>> medico = PersonalMedico.objects.create(usuario=usuario_medico, especialidad='Cardiología')
    >>> administrativo = PersonalAdministrativo.objects.create(usuario=usuario_administrativo, departamento='Recepción')

    >>> # Crear un certificado médico
    >>> certificado = CertificadoMedico.objects.create(
    ...     idconsulta=1,
    ...     paciente=paciente,
    ...     medico=medico,
    ...     administrativo=administrativo
    ... )

    >>> # Verificar el certificado
    >>> certificado.idconsulta
    1
    >>> certificado.paciente.direccion
    'Calle 123'
    >>> certificado.medico.especialidad
    'Cardiología'
    >>> certificado.administrativo.departamento
    'Recepción'

    >>> # Ver la representación del certificado
    >>> expected=f'Certificado {certificado.id} - {certificado.fecha_emision}'
    >>> assert(str(certificado))==expected
    """

    idconsulta = models.IntegerField()  # ID de la consulta asociada
    fecha_emision = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(PersonalMedico, on_delete=models.CASCADE)
    administrativo = models.ForeignKey(PersonalAdministrativo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Certificado {self.id} - {self.fecha_emision}"
