from ..modelos.administrador import Administrador

class AdministradorRepositorio:
    def get_all(self):
        return Administrador.objects.all()

    def get_by_id(self, admin_id):
        return Administrador.objects.get(id=admin_id)

    def create(self, data):
        administrador = Administrador.objects.create(**data)
        return administrador

    def update(self, admin_id, data):
        administrador = self.get_by_id(admin_id)
        for attr, value in data.items():
            setattr(administrador, attr, value)
        administrador.save()
        return administrador

    def delete(self, admin_id):
        administrador = self.get_by_id(admin_id)
        administrador.delete()
