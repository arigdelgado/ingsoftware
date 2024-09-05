from ..modelos.personal_administrativo import PersonalAdministrativo

class PersonalAdministrativoRepositorio:
    def get_all(self):
        return PersonalAdministrativo.objects.all()

    def get_by_id(self, administrativo_id):
        return PersonalAdministrativo.objects.get(id=administrativo_id)

    def create(self, data):
        administrativo = PersonalAdministrativo.objects.create(**data)
        return administrativo

    def update(self, administrativo_id, data):
        administrativo = self.get_by_id(administrativo_id)
        for attr, value in data.items():
            setattr(administrativo, attr, value)
        administrativo.save()
        return administrativo

    def delete(self, administrativo_id):
        administrativo = self.get_by_id(administrativo_id)
        administrativo.delete()
