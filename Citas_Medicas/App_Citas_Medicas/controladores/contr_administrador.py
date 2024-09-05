from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_administrador import AdministradorServicio

# Controlador para manejar las operaciones CRUD de Administrador
class AdministradorControlador(APIView):
    # Constructor que inicializa el servicio que maneja la lógica de negocio
    def __init__(self, *args, **kwargs):
        self.servicio = AdministradorServicio()  # Inicializa el servicio de administrador
        super().__init__(*args, **kwargs)

    # Método GET: obtiene un administrador por ID o una lista de todos los administradores
    def get(self, request, admin_id=None):
        if admin_id:  # Si se proporciona un ID de administrador
            data = self.servicio.obtener_por_id(admin_id)  # Llama al servicio para obtener el administrador
            return Response(data, status=status.HTTP_200_OK)  # Retorna la respuesta con los datos y código 200
        data = self.servicio.obtener_todos()  # Si no hay ID, obtiene todos los administradores
        return Response(data, status=status.HTTP_200_OK)  # Retorna la respuesta con todos los datos

    # Método POST: crea un nuevo administrador
    def post(self, request):
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.crear(data)  # Llama al servicio para crear un nuevo administrador
        return Response(result, status=status.HTTP_201_CREATED)  # Retorna la respuesta con el estado 201 (creado)

    # Método PUT: actualiza un administrador existente
    def put(self, request, admin_id):
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.actualizar(admin_id, data)  # Llama al servicio para actualizar el administrador
        return Response(result, status=status.HTTP_200_OK)  # Retorna la respuesta con los datos actualizados

    # Método DELETE: elimina un administrador por su ID
    def delete(self, request, admin_id):
        result = self.servicio.eliminar(admin_id)  # Llama al servicio para eliminar el administrador
        return Response(result, status=status.HTTP_204_NO_CONTENT)  # Retorna el estado 204 (sin contenido)
