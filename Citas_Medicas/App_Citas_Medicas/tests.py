import doctest
from django.test import TestCase
from App_Citas_Medicas.modelos import paciente
from App_Citas_Medicas.repositorios import rep_paciente
from App_Citas_Medicas.servicios import serv_paciente
from App_Citas_Medicas.modelos import certificado_medico
from App_Citas_Medicas.repositorios import rep_certificado_medico
from App_Citas_Medicas.servicios import serv_certificado_medico
from App_Citas_Medicas.modelos import administrador
from App_Citas_Medicas.repositorios import rep_administrador
from App_Citas_Medicas.servicios import serv_administrador

class DoctestTestCase(TestCase):
    def test_doctests(self):
        doctest.testmod(paciente)
        doctest.testmod(rep_paciente)
        doctest.testmod(serv_paciente)
        doctest.testmod(certificado_medico)
        doctest.testmod(rep_certificado_medico)
        doctest.testmod(serv_certificado_medico)
        doctest.testmod(administrador)
        doctest.testmod(rep_administrador)
        doctest.testmod(serv_administrador)
