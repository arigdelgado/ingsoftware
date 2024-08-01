from ..repositorios.rep_personal_medico import PersonalMedicoRepositorio
from ..serializers import PersonalMedicoSerializer

class PersonalMedicoServicio:
    def __init__(self):
        self.repositorio = PersonalMedicoRepositorio()

    def obtener_todos(self):
        medicos = self.repositorio.get_all()
        serializer = PersonalMedicoSerializer(medicos, many=True)
        return serializer.data

    def obtener_por_id(self, medico_id):
        medico = self.repositorio.get_by_id(medico_id)
        serializer = PersonalMedicoSerializer(medico)
        return serializer.data

    def crear(self, data):
        medico = self.repositorio.create(data)
        serializer = PersonalMedicoSerializer(medico)
        return serializer.data

    def actualizar(self, medico_id, data):
        medico = self.repositorio.update(medico_id, data)
        serializer = PersonalMedicoSerializer(medico)
        return serializer.data

    def eliminar(self, medico_id):
        self.repositorio.delete(medico_id)
        return {'mensaje': 'Personal médico eliminado'}