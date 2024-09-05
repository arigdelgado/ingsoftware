from ..modelos.certificado_medico import CertificadoMedico

class CertificadoMedicoRepositorio:
    """
    >>> from App_Citas_Medicas.modelos.certificado_medico import CertificadoMedico
    >>> from App_Citas_Medicas.modelos.paciente import Paciente
    >>> from App_Citas_Medicas.modelos.personal_medico import PersonalMedico
    >>> from App_Citas_Medicas.modelos.personal_administrativo import PersonalAdministrativo
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.repositorios.rep_certificado_medico import CertificadoMedicoRepositorio

    >>> # Crear instancias para las pruebas
    >>> usuario_paciente = Usuario.objects.create(nombre_completo='paciente', correo='paciente456@example.com', tipo_usuario='Paciente')
    >>> usuario_medico = Usuario.objects.create(nombre_completo='medico', correo='medico456@example.com', tipo_usuario='Medico')
    >>> usuario_administrativo = Usuario.objects.create(nombre_completo='admin', correo='admin456@example.com', tipo_usuario='Administrativo')
    
    >>> paciente = Paciente.objects.create(usuario=usuario_paciente, direccion='Calle 123', telefono='0915874236', historial_medico='Regular')
    >>> medico = PersonalMedico.objects.create(usuario=usuario_medico, especialidad='Cardiología')
    >>> administrativo = PersonalAdministrativo.objects.create(usuario=usuario_administrativo, departamento='Recepción')

    >>> repositorio = CertificadoMedicoRepositorio()

    >>> # Crear un certificado médico
    >>> data = {
    ...     'idconsulta': 4,
    ...     'paciente': paciente,
    ...     'medico': medico,
    ...     'administrativo': administrativo
    ... }
    >>> certificado = repositorio.create(data)
    >>> certificado.idconsulta
    4
    >>> certificado.paciente == paciente
    True

    >>> # Obtener todos los certificados
    >>> certificados = repositorio.get_all()
    >>> len(certificados) > 0
    True

    >>> # Obtener certificado por ID
    >>> certificado_id = certificado.id
    >>> certificado_obtenido = repositorio.get_by_id(certificado_id)
    >>> certificado_obtenido.idconsulta
    4

    >>> # Actualizar el certificado
    >>> data_actualizada = {
    ...     'idconsulta': 5
    ... }
    >>> certificado_actualizado = repositorio.update(certificado_id, data_actualizada)
    >>> certificado_actualizado.idconsulta
    5

    >>> # Eliminar el certificado
    >>> repositorio.delete(certificado_id)
    """

    def get_all(self):
        return CertificadoMedico.objects.all()

    def get_by_id(self, certificado_id):
        return CertificadoMedico.objects.get(id=certificado_id)

    def create(self, data):
        certificado = CertificadoMedico.objects.create(**data)
        return certificado

    def update(self, certificado_id, data):
        certificado = self.get_by_id(certificado_id)
        for attr, value in data.items():
            setattr(certificado, attr, value)
        certificado.save()
        return certificado

    def delete(self, certificado_id):
        certificado = self.get_by_id(certificado_id)
        certificado.delete()