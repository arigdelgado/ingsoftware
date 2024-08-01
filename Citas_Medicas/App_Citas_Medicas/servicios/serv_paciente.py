from ..repositorios.rep_paciente import PacienteRepositorio
from ..serializers import PacienteSerializer

class PacienteServicio:
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
        return {'mensaje': 'Paciente eliminado'}
