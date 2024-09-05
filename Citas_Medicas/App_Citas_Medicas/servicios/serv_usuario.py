from ..repositorios.rep_usuario import UsuarioRepositorio
from ..serializers import UsuarioSerializer

class UsuarioServicio:
    def __init__(self):
        self.repositorio = UsuarioRepositorio()

    def obtener_todos(self):
        usuarios = self.repositorio.get_all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return serializer.data

    def obtener_por_id(self, user_id):
        usuario = self.repositorio.get_by_id(user_id)
        serializer = UsuarioSerializer(usuario)
        return serializer.data

    def crear(self, data):
        usuario = self.repositorio.create(data)
        serializer = UsuarioSerializer(usuario)
        return serializer.data

    def actualizar(self, user_id, data):
        usuario = self.repositorio.update(user_id, data)
        serializer = UsuarioSerializer(usuario)
        return serializer.data

    def eliminar(self, user_id):
        self.repositorio.delete(user_id)
        return {'mensaje': 'Usuario eliminado'}
