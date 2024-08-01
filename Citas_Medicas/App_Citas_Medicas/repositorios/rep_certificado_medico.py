from ..modelos.certificado_medico import CertificadoMedico

class CertificadoMedicoRepositorio:
    def get_all(self):
        return CertificadoMedico.objects.all()

    def get_by_id(self, certificado_id):
        return CertificadoMedico.objects.get(id=certificado_id)

    def create(self, data):
        certificado = CertificadoMedico.objects.create(**data)
        return certificado

    def update(self, certificado_id, data):
        certificado = self.get_by_id(certificado_id)
        for attr, value in data.items():
            setattr(certificado, attr, value)
        certificado.save()
        return certificado

    def delete(self, certificado_id):
        certificado = self.get_by_id(certificado_id)
        certificado.delete()
