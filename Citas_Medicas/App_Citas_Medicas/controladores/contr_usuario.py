from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_usuario import UsuarioServicio

class UsuarioControlador(APIView):  # Define la clase UsuarioControlador que hereda de APIView
    def __init__(self, *args, **kwargs):  # Método constructor de la clase
        self.servicio = UsuarioServicio()  # Inicializa el servicio de usuario
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base

    def get(self, request, user_id=None):  # Método GET para obtener datos
        if user_id:  # Si se proporciona un user_id
            data = self.servicio.obtener_por_id(user_id)  # Obtiene el usuario por id
            return Response(data, status=status.HTTP_200_OK)  # Devuelve los datos con estado 200 OK
        data = self.servicio.obtener_todos()  # Si no se proporciona user_id, obtiene todos los usuarios
        return Response(data, status=status.HTTP_200_OK)  # Devuelve los datos con estado 200 OK

    def post(self, request):  # Método POST para crear un nuevo usuario
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.crear(data)  # Crea un nuevo usuario con los datos proporcionados
        return Response(result, status=status.HTTP_201_CREATED)  # Devuelve el resultado con estado 201 CREATED

    def put(self, request, user_id):  # Método PUT para actualizar un usuario existente
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.actualizar(user_id, data)  # Actualiza el usuario con los nuevos datos
        return Response(result, status=status.HTTP_200_OK)  # Devuelve el resultado con estado 200 OK

    def delete(self, request, user_id):  # Método DELETE para eliminar un usuario
        result = self.servicio.eliminar(user_id)  # Elimina el usuario por id
        return Response(result, status=status.HTTP_204_NO_CONTENT)  # Devuelve el resultado con estado 204 NO CONTENT
