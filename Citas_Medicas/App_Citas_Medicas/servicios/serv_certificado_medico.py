from ..repositorios.rep_certificado_medico import CertificadoMedicoRepositorio
from ..serializers import CertificadoMedicoSerializer

class CertificadoMedicoServicio:
    """
    >>> from App_Citas_Medicas.modelos.certificado_medico import CertificadoMedico
    >>> from App_Citas_Medicas.modelos.paciente import Paciente
    >>> from App_Citas_Medicas.modelos.personal_medico import PersonalMedico
    >>> from App_Citas_Medicas.modelos.personal_administrativo import PersonalAdministrativo
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.servicios.serv_certificado_medico import CertificadoMedicoServicio

    >>> # Crear instancias para las pruebas
    >>> usuario_paciente = Usuario.objects.create(nombre_completo='paciente', correo='paciente582@gmail.com', tipo_usuario='Paciente')
    >>> usuario_medico = Usuario.objects.create(nombre_completo='medico', correo='medico582@gmail.com', tipo_usuario='Medico')
    >>> usuario_administrativo = Usuario.objects.create(nombre_completo='admin', correo='admin582@gmail.com', tipo_usuario='Administrativo')
   
    >>> paciente = Paciente.objects.create(usuario=usuario_paciente, direccion='Calle 123', telefono='0915874236', historial_medico='Regular')
    >>> medico = PersonalMedico.objects.create(usuario=usuario_medico, especialidad='Cardiología')
    >>> administrativo = PersonalAdministrativo.objects.create(usuario=usuario_administrativo, departamento='Recepción')

    >>> servicio = CertificadoMedicoServicio()

    >>> # Crear un certificado médico
    >>> data = {
    ...     'idconsulta': 2,
    ...     'paciente': paciente,
    ...     'medico': medico,
    ...     'administrativo': administrativo
    ... }
    >>> certificado = servicio.crear(data)

    >>> # Obtener todos los certificados
    >>> certificados = servicio.obtener_todos()
    >>> len(certificados) > 0
    True

    >>> # Obtener certificado por ID
    >>> certificado_id = certificado['id']
    >>> certificado_obtenido = servicio.obtener_por_id(certificado_id)
    >>> assert certificado_obtenido['idconsulta'] == 2

    >>> # Actualizar el certificado
    >>> data_actualizada = {
    ...     'idconsulta': 3,
    ...     'paciente': paciente,
    ...     'medico': medico,
    ...     'administrativo': administrativo
    ... }
    >>> certificado_actualizado = servicio.actualizar(certificado_id, data_actualizada)
    >>> assert certificado_actualizado['idconsulta'] == 3

    >>> # Eliminar el certificado
    >>> mensaje = servicio.eliminar(certificado_id)
    >>> assert mensaje['mensaje'] == 'Certificado médico eliminado'
    """

    def __init__(self):
        self.repositorio = CertificadoMedicoRepositorio()

    def obtener_todos(self):
        certificados = self.repositorio.get_all()
        serializer = CertificadoMedicoSerializer(certificados, many=True)
        return serializer.data

    def obtener_por_id(self, certificado_id):
        certificado = self.repositorio.get_by_id(certificado_id)
        serializer = CertificadoMedicoSerializer(certificado)
        return serializer.data

    def crear(self, data):
        certificado = self.repositorio.create(data)
        serializer = CertificadoMedicoSerializer(certificado)
        return serializer.data

    def actualizar(self, certificado_id, data):
        certificado = self.repositorio.update(certificado_id, data)
        serializer = CertificadoMedicoSerializer(certificado)
        return serializer.data

    def eliminar(self, certificado_id):
        self.repositorio.delete(certificado_id)
        return {'mensaje': 'Certificado médico eliminado'}