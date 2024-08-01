from rest_framework import serializers
from App_Citas_Medicas.modelos import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre_completo', 'tipo_usuario']

class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Paciente
        fields = ['id', 'usuario', 'direccion', 'telefono', 'historial_medico']

class AdministradorSerializer(serializers.ModelSerializer):
     # Serializador anidado para incluir detalles del usuario
    usuario = UsuarioSerializer()

    class Meta:
        model = Administrador
        fields = ['id', 'usuario', 'permisos']

class PersonalMedicoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = PersonalMedico
        fields = ['id', 'usuario', 'especialidad']

class PersonalAdministrativoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = PersonalAdministrativo
        fields = ['id', 'usuario', 'departamento']

class CertificadoMedicoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    medico = PersonalMedicoSerializer()
    administrativo = PersonalAdministrativoSerializer()

    class Meta:
        model = CertificadoMedico
        fields = ['id', 'idconsulta', 'fecha_emision', 'paciente', 'medico', 'administrativo']
