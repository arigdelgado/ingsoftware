from .rep_usuario import UsuarioRepositorio
from .rep_paciente import PacienteRepositorio
from .rep_administrador import AdministradorRepositorio
from .rep_personal_medico import PersonalMedicoRepositorio
from .rep_personal_administrativo import PersonalAdministrativoRepositorio
from .rep_certificado_medico import CertificadoMedicoRepositorio

__all__ = [
    'UsuarioRepositorio',
    'PacienteRepositorio',
    'AdministradorRepositorio',
    'PersonalMedicoRepositorio',
    'PersonalAdministrativoRepositorio',
    'CertificadoMedicoRepositorio',
]