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

    def test_regra2_compras_acima_de_1000_recebem_20_porcento_desconto(self):
        self.assertEqual(self.calculadora.calcular_pedido(1500.0), 1200.0)
        self.assertEqual(self.calculadora.calcular_pedido(1000.01), 800.01)
        self.assertEqual(self.calculadora.calcular_pedido(1000.0), 900.0)

    def test_regra3_cliente_vip_ganha_5_porcento_desconto_adicional(self):
        self.assertEqual(self.calculadora.calcular_pedido(200.0, vip=True), 190.0)
        self.assertEqual(self.calculadora.calcular_pedido(600.0, vip=True), 513.0)
        self.assertEqual(self.calculadora.calcular_pedido(1500.0, vip=True), 1140.0)

    def test_regra4_frete_fixo_15_para_valor_final_inferior_a_100(self):
        self.assertEqual(self.calculadora.calcular_pedido(80.0), 95.0)
        self.assertEqual(self.calculadora.calcular_pedido(100.0, vip=False), 100.0)
        self.assertEqual(self.calculadora.calcular_pedido(100.0, vip=True), 110.0)

    def test_regra5_pedido_zerado_ou_negativo_lanca_excecao(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_pedido(0.0)
        with self.assertRaises(ValueError):
            self.calculadora.calcular_pedido(-50.0)
        with self.assertRaises(ValueError):
            self.calculadora.calcular_compra(0, 100.0)
        with self.assertRaises(ValueError):
            self.calculadora.calcular_compra(2, -50.0)


if __name__ == "__main__":
    unittest.main()
