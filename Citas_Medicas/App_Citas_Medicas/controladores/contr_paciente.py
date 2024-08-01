from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_paciente import PacienteServicio

class PacienteControlador(APIView):
    def __init__(self, *args, **kwargs):
        self.servicio = PacienteServicio()
        super().__init__(*args, **kwargs)

    def get(self, request, paciente_id=None):
        if paciente_id:
            data = self.servicio.obtener_por_id(paciente_id)
            return Response(data, status=status.HTTP_200_OK)
        data = self.servicio.obtener_todos()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        result = self.servicio.crear(data)
        return Response(result, status=status.HTTP_201_CREATED)

    def put(self, request, paciente_id):
        data = request.data
        result = self.servicio.actualizar(paciente_id, data)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, paciente_id):
        result = self.servicio.eliminar(paciente_id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
