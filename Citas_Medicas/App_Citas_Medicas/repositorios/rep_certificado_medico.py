from ..modelos.certificado_medico import CertificadoMedico

# Definición de la clase CertificadoMedicoRepositorio
class CertificadoMedicoRepositorio:
    # Método para obtener todos los certificados médicos
    def get_all(self):
        return CertificadoMedico.objects.all()

    # Método para obtener un certificado médico por su ID
    def get_by_id(self, certificado_id):
        return CertificadoMedico.objects.get(id=certificado_id)

    # Método para crear un nuevo certificado médico
    # data es un diccionario con los datos necesarios para crear el certificado
    def create(self, data):
        certificado = CertificadoMedico.objects.create(**data)
        return certificado

    # Método para actualizar un certificado médico existente
    # certificado_id es el ID del certificado a actualizar
    # data es un diccionario con los datos a actualizar
    def update(self, certificado_id, data):
        certificado = self.get_by_id(certificado_id)
        for attr, value in data.items():
            setattr(certificado, attr, value)
        certificado.save()
        return certificado

    # Método para eliminar un certificado médico por su ID
    def delete(self, certificado_id):
        certificado = self.get_by_id(certificado_id)
        certificado.delete()
