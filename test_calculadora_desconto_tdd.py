import unittest
from calculadora_desconto_tdd import CalculadoraDescontoTDD


class TestCalculadoraDescontoTDD(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraDescontoTDD()

    def test_regra1_compras_acima_de_500_recebem_10_porcento_desconto(self):
        self.assertEqual(self.calculadora.calcular_pedido(600.0), 540.0)
        self.assertEqual(self.calculadora.calcular_pedido(500.01), 450.01)
        self.assertEqual(self.calculadora.calcular_pedido(500.0), 500.0)
        self.assertEqual(self.calculadora.calcular_pedido(200.0), 200.0)


if __name__ == "__main__":
    unittest.main()
