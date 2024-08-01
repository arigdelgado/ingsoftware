from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_personal_administrativo import PersonalAdministrativoServicio

class PersonalAdministrativoControlador(APIView):
    def __init__(self, *args, **kwargs):
        self.servicio = PersonalAdministrativoServicio()
        super().__init__(*args, **kwargs)

    def get(self, request, administrativo_id=None):
        if administrativo_id:
            data = self.servicio.obtener_por_id(administrativo_id)
            return Response(data, status=status.HTTP_200_OK)
        data = self.servicio.obtener_todos()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        result = self.servicio.crear(data)
        return Response(result, status=status.HTTP_201_CREATED)

    def put(self, request, administrativo_id):
        data = request.data
        result = self.servicio.actualizar(administrativo_id, data)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, administrativo_id):
        result = self.servicio.eliminar(administrativo_id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
