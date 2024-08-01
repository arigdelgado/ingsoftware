#Contr_administrador
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_administrador import AdministradorServicio

class AdministradorControlador(APIView):  # Define la clase AdministradorControlador que hereda de APIView
    def __init__(self, *args, **kwargs):  # Método constructor de la clase
        self.servicio = AdministradorServicio()  # Inicializa el servicio de administrador
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base

    def get(self, request, admin_id=None):  # Método GET para obtener datos
        if admin_id:  # Si se proporciona un admin_id
            data = self.servicio.obtener_por_id(admin_id)  # Obtiene el administrador por id
            return Response(data, status=status.HTTP_200_OK)  # Devuelve los datos con estado 200 OK
        data = self.servicio.obtener_todos()  # Si no se proporciona admin_id, obtiene todos los administradores
        return Response(data, status=status.HTTP_200_OK)  # Devuelve los datos con estado 200 OK

    def post(self, request):  # Método POST para crear un nuevo administrador
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.crear(data)  # Crea un nuevo administrador con los datos proporcionados
        return Response(result, status=status.HTTP_201_CREATED)  # Devuelve el resultado con estado 201 CREATED

    def put(self, request, admin_id):  # Método PUT para actualizar un administrador existente
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.actualizar(admin_id, data)  # Actualiza el administrador con los nuevos datos
        return Response(result, status=status.HTTP_200_OK)  # Devuelve el resultado con estado 200 OK

    def delete(self, request, admin_id):  # Método DELETE para eliminar un administrador
        result = self.servicio.eliminar(admin_id)  # Elimina el administrador por id
        return Response(result, status=status.HTTP_204_NO_CONTENT)  # Devuelve el resultado con estado 204 NO CONTENT

