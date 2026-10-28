import unittest
from calculadora_desconto_tradicional import CalculadoraDescontoTradicional


class TestCalculadoraDescontoTradicional(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraDescontoTradicional()

    def test_compra_sem_desconto_sem_frete(self):
        # Compra de R$ 200,00 (>= 100 e <= 500): sem desconto e sem frete
        self.assertEqual(self.calculadora.calcular_compra(2, 100.0, vip=False), 200.00)
        # Limite exato de R$ 500,00: ainda sem desconto
        self.assertEqual(self.calculadora.calcular_compra(5, 100.0, vip=False), 500.00)

    def test_compra_acima_de_500_recebe_10_porcento_desconto(self):
        # Compra de R$ 600,00 -> 10% de desconto = R$ 540,00
        self.assertEqual(self.calculadora.calcular_compra(6, 100.0, vip=False), 540.00)
        # Limite exato de R$ 1.000,00 -> 10% de desconto = R$ 900,00
        self.assertEqual(self.calculadora.calcular_compra(10, 100.0, vip=False), 900.00)

    def test_compra_acima_de_1000_recebe_20_porcento_desconto(self):
        # Compra de R$ 1.500,00 -> 20% de desconto = R$ 1.200,00
        self.assertEqual(self.calculadora.calcular_compra(3, 500.0, vip=False), 1200.00)

    def test_cliente_vip_recebe_5_porcento_adicional_sobre_valor_com_desconto(self):
        # Sem desconto de faixa: R$ 200,00 -> VIP 5% = R$ 190,00
        self.assertEqual(self.calculadora.calcular_compra(2, 100.0, vip=True), 190.00)
        # Com 10% de desconto: R$ 600,00 -> R$ 540,00 -> VIP 5% = R$ 513,00
        self.assertEqual(self.calculadora.calcular_compra(6, 100.0, vip=True), 513.00)
        # Com 20% de desconto: R$ 1.500,00 -> R$ 1.200,00 -> VIP 5% = R$ 1.140,00
        self.assertEqual(self.calculadora.calcular_compra(3, 500.0, vip=True), 1140.00)

    def test_frete_fixo_para_valor_final_inferior_a_100(self):
        # Compra de R$ 80,00 (< 100) -> + R$ 15,00 de frete = R$ 95,00
        self.assertEqual(self.calculadora.calcular_compra(1, 80.0, vip=False), 95.00)
        # Compra de R$ 100,00 sem VIP -> exatamente R$ 100,00 (sem frete)
        self.assertEqual(self.calculadora.calcular_compra(1, 100.0, vip=False), 100.00)
        # Compra de R$ 100,00 com VIP -> R$ 95,00 após desconto (< 100) -> + R$ 15,00 frete = R$ 110,00
        self.assertEqual(self.calculadora.calcular_compra(1, 100.0, vip=True), 110.00)

    def test_pedido_com_valor_zerado_ou_negativo_lanca_excecao(self):
        with self.assertRaises(ValueError):
            self.calculadora.calcular_compra(0, 100.0)
        with self.assertRaises(ValueError):
            self.calculadora.calcular_compra(1, 0.0)
        with self.assertRaises(ValueError):
            self.calculadora.calcular_compra(-2, 50.0)
        with self.assertRaises(ValueError):
            self.calculadora.calcular_compra(2, -50.0)


if __name__ == "__main__":
    unittest.main()
