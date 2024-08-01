from ..repositorios.rep_administrador import AdministradorRepositorio
from ..serializers import AdministradorSerializer

class AdministradorServicio:
    def __init__(self):
        self.repositorio = AdministradorRepositorio()

    def obtener_todos(self):
        administradores = self.repositorio.get_all()
        serializer = AdministradorSerializer(administradores, many=True)
        return serializer.data

    def obtener_por_id(self, admin_id):
        administrador = self.repositorio.get_by_id(admin_id)
        serializer = AdministradorSerializer(administrador)
        return serializer.data

    def crear(self, data):
        administrador = self.repositorio.create(data)
        serializer = AdministradorSerializer(administrador)
        return serializer.data

    def actualizar(self, admin_id, data):
        administrador = self.repositorio.update(admin_id, data)
        serializer = AdministradorSerializer(administrador)
        return serializer.data

    def eliminar(self, admin_id):
        self.repositorio.delete(admin_id)
        return {'mensaje': 'Administrador eliminado'}