from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_personal_medico import PersonalMedicoServicio

class PersonalMedicoControlador(APIView):
    def __init__(self, *args, **kwargs):
        self.servicio = PersonalMedicoServicio()
        super().__init__(*args, **kwargs)

    def get(self, request, medico_id=None):
        if medico_id:
            data = self.servicio.obtener_por_id(medico_id)
            return Response(data, status=status.HTTP_200_OK)
        data = self.servicio.obtener_todos()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        result = self.servicio.crear(data)
        return Response(result, status=status.HTTP_201_CREATED)

    def put(self, request, medico_id):
        data = request.data
        result = self.servicio.actualizar(medico_id, data)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, medico_id):
        result = self.servicio.eliminar(medico_id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
