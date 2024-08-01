from ..repositorios.rep_certificado_medico import CertificadoMedicoRepositorio
from ..serializers import CertificadoMedicoSerializer

class CertificadoMedicoServicio:
    def __init__(self):
        self.repositorio = CertificadoMedicoRepositorio()

    def obtener_todos(self):
        certificados = self.repositorio.get_all()
        serializer = CertificadoMedicoSerializer(certificados, many=True)
        return serializer.data

    def obtener_por_id(self, certificado_id):
        certificado = self.repositorio.get_by_id(certificado_id)
        serializer = CertificadoMedicoSerializer(certificado)
        return serializer.data

    def crear(self, data):
        certificado = self.repositorio.create(data)
        serializer = CertificadoMedicoSerializer(certificado)
        return serializer.data

    def actualizar(self, certificado_id, data):
        certificado = self.repositorio.update(certificado_id, data)
        serializer = CertificadoMedicoSerializer(certificado)
        return serializer.data

    def eliminar(self, certificado_id):
        self.repositorio.delete(certificado_id)
        return {'mensaje': 'Certificado médico eliminado'}