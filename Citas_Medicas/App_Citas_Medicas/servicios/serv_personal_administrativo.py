from ..repositorios.rep_personal_administrativo import PersonalAdministrativoRepositorio
from ..serializers import PersonalAdministrativoSerializer

class PersonalAdministrativoServicio:
    def __init__(self):
        self.repositorio = PersonalAdministrativoRepositorio()

    def obtener_todos(self):
        administrativos = self.repositorio.get_all()
        serializer = PersonalAdministrativoSerializer(administrativos, many=True)
        return serializer.data

    def obtener_por_id(self, administrativo_id):
        administrativo = self.repositorio.get_by_id(administrativo_id)
        serializer = PersonalAdministrativoSerializer(administrativo)
        return serializer.data

    def crear(self, data):
        administrativo = self.repositorio.create(data)
        serializer = PersonalAdministrativoSerializer(administrativo)
        return serializer.data

    def actualizar(self, administrativo_id, data):
        administrativo = self.repositorio.update(administrativo_id, data)
        serializer = PersonalAdministrativoSerializer(administrativo)
        return serializer.data

    def eliminar(self, administrativo_id):
        self.repositorio.delete(administrativo_id)
        return {'mensaje': 'Personal administrativo eliminado'}