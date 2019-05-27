from src.c import *
from src.g import *
from scripts.d import *

import unittest


class TestC(unittest.TestCase):

    def setUp(self):
        pass

    def test_test(self):
        assert True == True, "Teste testado."

    def testa_c(self):
        assert None == faz_c(), "Faz c testado."

    def testa_g(self):
        assert 'G' == faz_g(), "Faz g testado."

    def testa_d(self):
        assert None == faz_d(), "Faz d testado."
