from ..modelos.personal_medico import PersonalMedico

class PersonalMedicoRepositorio:
    def get_all(self):
        return PersonalMedico.objects.all()

    def get_by_id(self, medico_id):
        return PersonalMedico.objects.get(id=medico_id)

    def create(self, data):
        medico = PersonalMedico.objects.create(**data)
        return medico

    def update(self, medico_id, data):
        medico = self.get_by_id(medico_id)
        for attr, value in data.items():
            setattr(medico, attr, value)
        medico.save()
        return medico

    def delete(self, medico_id):
        medico = self.get_by_id(medico_id)
        medico.delete()
