from ..repositorios.rep_administrador import AdministradorRepositorio
from ..serializers import AdministradorSerializer

class AdministradorServicio:
    """
    >>> from App_Citas_Medicas.modelos.usuario import Usuario
    >>> from App_Citas_Medicas.modelos.administrador import Administrador
    >>> from App_Citas_Medicas.servicios.serv_administrador import AdministradorServicio

    >>> # Crear un usuario
    >>> usuario = Usuario.objects.create(nombre_completo='Ximena Parra', correo='ximena_parra@gmail.com', tipo_usuario='Administrador')

    >>> # Crear el servicio de administrador
    >>> servicio = AdministradorServicio()

    >>> # Crear un administrador usando el servicio
    >>> data = {'usuario': usuario, 'permisos': 'admin'}
    >>> administrador = servicio.crear(data)

    >>> # Verificar que el administrador se creó correctamente
    >>> administrador['usuario']['nombre_completo']
    'Ximena Parra'

    >>> # Obtener todos los administradores
    >>> all_admins = servicio.obtener_todos()
    >>> len(all_admins) > 0
    True

    >>> # Obtener un administrador por ID
    >>> admin_obtenido = servicio.obtener_por_id(administrador['id'])
    >>> admin_obtenido['usuario']['nombre_completo']
    'Ximena Parra'

    >>> # Actualizar un administrador
    >>> data_actualizada = {'permisos': 'admin, manage, edit'}
    >>> admin_actualizado = servicio.actualizar(administrador['id'], data_actualizada)
    >>> admin_actualizado['permisos']
    'admin, manage, edit'

    >>> # Eliminar un administrador
    >>> mensaje = servicio.eliminar(administrador['id'])
    >>> mensaje['mensaje']
    'Administrador eliminado'
    """

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