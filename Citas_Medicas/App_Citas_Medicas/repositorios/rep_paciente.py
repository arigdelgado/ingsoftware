from ..modelos.paciente import Paciente

class PacienteRepositorio:
    def get_all(self):
        return Paciente.objects.all()

    def get_by_id(self, paciente_id):
        return Paciente.objects.get(id=paciente_id)

    def create(self, data):
        paciente = Paciente.objects.create(**data)
        return paciente

    def update(self, paciente_id, data):
        paciente = self.get_by_id(paciente_id)
        for attr, value in data.items():
            setattr(paciente, attr, value)
        paciente.save()
        return paciente

    def delete(self, paciente_id):
        paciente = self.get_by_id(paciente_id)
        paciente.delete()
