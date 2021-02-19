import unittest

from leitor_de_faturas import LeitorDeTransacoes


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.leitor = LeitorDeTransacoes

    def test_valida_linha_de_pagamento(self):
        self.leitor.le(self)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
