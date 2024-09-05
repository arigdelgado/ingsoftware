from ..modelos.paciente import Paciente

class PacienteRepositorio:
    """
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.modelos.paciente import Paciente
    >>> from App_Citas_Medicas.repositorios.rep_paciente import PacienteRepositorio
    >>> from django.contrib.auth.models import User

    >>> # Crear un usuario y un paciente para las pruebas
    >>> user = User.objects.create_user(username='pedro', password='secret')
    >>> usuario = Usuario.objects.create(id=user.id, nombre_completo='pedro', correo='pedro@gmail.com', tipo_usuario='Paciente')
    >>> data = {'usuario': usuario, 'direccion': 'Calle 456', 'telefono': '0912345678', 'historial_medico': 'Ninguno'}
    >>> repo = PacienteRepositorio()

    >>> # Crear un paciente
    >>> paciente = repo.create(data)

    >>> # Obtener todos los pacientes
    >>> pacientes = repo.get_all()
    >>> len(pacientes) > 0
    True

    >>> # Obtener un paciente por ID
    >>> paciente_obtenido = repo.get_by_id(paciente.id)
    >>> paciente_obtenido.usuario.nombre_completo
    'pedro'

    >>> # Actualizar un paciente
    >>> updated_data = {'direccion': 'Nueva Dirección 456'}
    >>> paciente_actualizado = repo.update(paciente.id, updated_data)
    >>> paciente_actualizado.direccion
    'Nueva Dirección 456'

    >>> # Eliminar un paciente
    >>> repo.delete(paciente.id)
    """

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