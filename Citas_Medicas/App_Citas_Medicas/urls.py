from django.urls import path
from App_Citas_Medicas.controladores import *

################################################################
#rutasURL
################################################################
urlpatterns = [
    # Rutas para Usuarios
    path('usuarios/', UsuarioControlador.as_view(), name='usuario-list'),
    path('usuarios/<int:user_id>/', UsuarioControlador.as_view(), name='usuario-detail'),

    # Rutas para Pacientes
    path('pacientes/', PacienteControlador.as_view(), name='paciente-list'),
    path('pacientes/<int:paciente_id>/', PacienteControlador.as_view(), name='paciente-detail'),

    # Rutas para Administradores
    path('administradores/', AdministradorControlador.as_view(), name='administrador-list'),
    path('administradores/<int:admin_id>/', AdministradorControlador.as_view(), name='administrador-detail'),

    # Rutas para Personal Médico
    path('medicos/', PersonalMedicoControlador.as_view(), name='medico-list'),
    path('medicos/<int:medico_id>/', PersonalMedicoControlador.as_view(), name='medico-detail'),

    # Rutas para Personal Administrativo
    path('administrativos/', PersonalAdministrativoControlador.as_view(), name='administrativo-list'),
    path('administrativos/<int:administrativo_id>/', PersonalAdministrativoControlador.as_view(), name='administrativo-detail'),

    # Rutas para Certificados Médicos
    path('certificados/', CertificadoMedicoControlador.as_view(), name='certificado-list'),
    path('certificados/<int:certificado_id>/', CertificadoMedicoControlador.as_view(), name='certificado-detail'),
]
