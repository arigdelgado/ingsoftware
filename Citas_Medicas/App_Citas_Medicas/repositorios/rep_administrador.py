from ..modelos.administrador import Administrador

class AdministradorRepositorio:
    """
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.modelos.administrador import Administrador
    >>> from App_Citas_Medicas.repositorios.rep_administrador import AdministradorRepositorio

    >>> # Crear un usuario
    >>> usuario = Usuario.objects.create(nombre_completo='Ana Gómez', correo='anagomez@gmail.com', tipo_usuario='Administrador')

    >>> # Crear un repositorio de administrador
    >>> repositorio = AdministradorRepositorio()

    >>> # Crear un administrador usando el repositorio
    >>> data = {'usuario': usuario, 'permisos': 'admin, manage'}
    >>> administrador = repositorio.create(data)

    >>> # Verificar que el administrador se creó correctamente
    >>> administrador.usuario.nombre_completo
    'Ana Gómez'

    >>> # Obtener todos los administradores
    >>> all_admins = repositorio.get_all()
    >>> len(all_admins) > 0
    True

    >>> # Obtener un administrador por ID
    >>> admin_obtenido = repositorio.get_by_id(administrador.id)
    >>> admin_obtenido.usuario.nombre_completo
    'Ana Gómez'

    >>> # Eliminar un administrador
    >>> repositorio.delete(administrador.id)
    """
    
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