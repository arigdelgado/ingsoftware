from ..modelos.usuario import Usuario

class UsuarioRepositorio:
    def get_all(self):
        return Usuario.objects.all()

    def get_by_id(self, user_id):
        return Usuario.objects.get(id=user_id)

    def create(self, data):
        usuario = Usuario.objects.create(**data)
        return usuario

    def update(self, user_id, data):
        usuario = self.get_by_id(user_id)
        for attr, value in data.items():
            setattr(usuario, attr, value)
        usuario.save()
        return usuario

    def delete(self, user_id):
        usuario = self.get_by_id(user_id)
        usuario.delete()
