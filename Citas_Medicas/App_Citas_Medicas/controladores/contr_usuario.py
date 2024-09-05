from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Importamos la clase UsuarioServicio desde el módulo servicios.serv_usuario
from ..servicios.serv_usuario import UsuarioServicio

# Definimos la clase UsuarioControlador que hereda de APIView
class UsuarioControlador(APIView):
    # Método constructor que se llama cuando se crea una instancia de la clase
    def __init__(self, *args, **kwargs):
        # Creamos una instancia de la clase UsuarioServicio y la asignamos a la variable self.servicio
        self.servicio = UsuarioServicio()
        # Llamamos al constructor de la clase padre (APIView)
        super().__init__(*args, **kwargs)

    # Método que se llama cuando se recibe una solicitud GET
    def get(self, request, user_id=None):
        # Si se proporciona un user_id, obtenemos el usuario correspondiente
        if user_id:
            # Llamamos al método obtener_por_id de la clase UsuarioServicio y asignamos el resultado a la variable data
            data = self.servicio.obtener_por_id(user_id)
            # Devolvemos una respuesta con el estado HTTP 200 OK y los datos del usuario
            return Response(data, status=status.HTTP_200_OK)
        # Si no se proporciona un user_id, obtenemos todos los usuarios
        else:
            # Llamamos al método obtener_todos de la clase UsuarioServicio y asignamos el resultado a la variable data
            data = self.servicio.obtener_todos()
            # Devolvemos una respuesta con el estado HTTP 200 OK y los datos de todos los usuarios
            return Response(data, status=status.HTTP_200_OK)

    # Método que se llama cuando se recibe una solicitud POST
    def post(self, request):
        # Obtenemos los datos de la solicitud
        data = request.data
        # Llamamos al método crear de la clase UsuarioServicio y asignamos el resultado a la variable result
        result = self.servicio.crear(data)
        # Devolvemos una respuesta con el estado HTTP 201 Created y los datos del usuario creado
        return Response(result, status=status.HTTP_201_CREATED)

    # Método que se llama cuando se recibe una solicitud PUT
    def put(self, request, user_id):
        # Obtenemos los datos de la solicitud
        data = request.data
        # Llamamos al método actualizar de la clase UsuarioServicio y asignamos el resultado a la variable result
        result = self.servicio.actualizar(user_id, data)
        # Devolvemos una respuesta con el estado HTTP 200 OK y los datos del usuario actualizado
        return Response(result, status=status.HTTP_200_OK)

    # Método que se llama cuando se recibe una solicitud DELETE
    def delete(self, request, user_id):
        # Llamamos al método eliminar de la clase UsuarioServicio y asignamos el resultado a la variable result
        result = self.servicio.eliminar(user_id)
        # Devolvemos una respuesta con el estado HTTP 204 No Content
        return Response(result, status=status.HTTP_204_NO_CONTENT)