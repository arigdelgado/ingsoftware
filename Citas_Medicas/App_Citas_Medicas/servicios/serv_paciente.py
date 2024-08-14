from ..repositorios.rep_paciente import PacienteRepositorio
from ..serializers import PacienteSerializer

class PacienteServicio:
    """
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.modelos.paciente import Paciente
    >>> from App_Citas_Medicas.repositorios.rep_paciente import PacienteRepositorio
    >>> from App_Citas_Medicas.servicios.serv_paciente import PacienteServicio
    >>> from django.contrib.auth.models import User
    
    >>> # Crear un usuario y un paciente para las pruebas
    >>> user = User.objects.create_user(username='juan', password='secret')
    >>> usuario = Usuario.objects.create(id=user.id, nombre_completo='juan', correo='juan@gmail.com', tipo_usuario='Paciente')
    >>> data = {'usuario': usuario, 'direccion': 'Calle 789', 'telefono': '0912345678', 'historial_medico': '2 Visitas'}
    >>> servicio = PacienteServicio()
    
    >>> # Crear un paciente
    >>> paciente_creado = servicio.crear(data)

    >>> # Obtener todos los pacientes
    >>> pacientes = servicio.obtener_todos()
    >>> len(pacientes) > 0
    True

    >>> # Obtener un paciente por ID
    >>> paciente_obtenido = servicio.obtener_por_id(paciente_creado['usuario']['id'])
    >>> paciente_obtenido['direccion']
    'Calle 789'

    >>> # Actualizar un paciente
    >>> updated_data = {'direccion': 'Nueva Dirección 789'}
    >>> paciente_actualizado = servicio.actualizar(paciente_creado['usuario']['id'], updated_data)
    >>> paciente_actualizado['direccion']
    'Nueva Dirección 789'

    >>> # Eliminar un paciente
    >>> servicio.eliminar(paciente_creado['usuario']['id'])
    """

    def __init__(self):
        self.repositorio = PacienteRepositorio()

    def obtener_todos(self):
        pacientes = self.repositorio.get_all()
        serializer = PacienteSerializer(pacientes, many=True)
        return serializer.data

    def obtener_por_id(self, paciente_id):
        paciente = self.repositorio.get_by_id(paciente_id)
        serializer = PacienteSerializer(paciente)
        return serializer.data

    def crear(self, data):
        paciente = self.repositorio.create(data)
        serializer = PacienteSerializer(paciente)
        return serializer.data

    def actualizar(self, paciente_id, data):
        paciente = self.repositorio.update(paciente_id, data)
        serializer = PacienteSerializer(paciente)
        return serializer.data

    def eliminar(self, paciente_id):
        self.repositorio.delete(paciente_id)