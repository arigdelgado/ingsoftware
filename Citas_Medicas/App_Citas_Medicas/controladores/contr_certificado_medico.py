from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..servicios.serv_certificado_medico import CertificadoMedicoServicio

class CertificadoMedicoControlador(APIView):
    def __init__(self, *args, **kwargs):
        self.servicio = CertificadoMedicoServicio()
        super().__init__(*args, **kwargs)

    def get(self, request, certificado_id=None):
        if certificado_id:
            data = self.servicio.obtener_por_id(certificado_id)
            return Response(data, status=status.HTTP_200_OK)
        data = self.servicio.obtener_todos()
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        result = self.servicio.crear(data)
        return Response(result, status=status.HTTP_201_CREATED)

    def put(self, request, certificado_id):
        data = request.data
        result = self.servicio.actualizar(certificado_id, data)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, certificado_id):
        result = self.servicio.eliminar(certificado_id)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
