from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_personal_medico import PersonalMedicoServicio

class PersonalMedicoControlador(APIView):  # Define la clase PersonalMedicoControlador que hereda de APIView
    def __init__(self, *args, **kwargs):  # Método constructor de la clase
        self.servicio = PersonalMedicoServicio()  # Inicializa el servicio de personal médico
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base

    def get(self, request, medico_id=None):  # Método GET para obtener los datos
        if medico_id:  # Si se proporciona un medico_id
            data = self.servicio.obtener_por_id(medico_id)  # Obtiene el médico por id
            return Response(data, status=status.HTTP_200_OK)  # Devuelve los datos con estado 200 OK
        data = self.servicio.obtener_todos()  # Si no se proporciona medico_id, obtiene todos los médicos
        return Response(data, status=status.HTTP_200_OK)  # Devuelve los datos con estado 200 

    def post(self, request):  # Método POST para crear un nuevo personal médico
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.crear(data)  # Crea un nuevo personal médico con los datos proporcionados
        return Response(result, status=status.HTTP_201_CREATED)  # Devuelve el resultado con estado 201 CREATED

    def put(self, request, medico_id):  # Método PUT para actualizar un personal médico existente
        data = request.data  # Obtiene los datos de la solicitud
        result = self.servicio.actualizar(medico_id, data)  # Actualiza el personal médico con los nuevos datos
        return Response(result, status=status.HTTP_200_OK)  # Devuelve el resultado con estado 200 OK

    def delete(self, request, medico_id):  # Método DELETE para eliminar un personal médico
        result = self.servicio.eliminar(medico_id)  # Elimina el personal médico por id
        return Response(result, status=status.HTTP_204_NO_CONTENT)  # Devuelve el resultado con estado 204 NO CONTENT

