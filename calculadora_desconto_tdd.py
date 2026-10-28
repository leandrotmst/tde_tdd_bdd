class CalculadoraDescontoTDD:
    LIMITE_DESCONTO_10 = 500.0
    TAXA_DESCONTO_10 = 0.10

    def calcular_pedido(self, valor_total: float, vip: bool = False) -> float:
        valor_final = valor_total
        if valor_total > self.LIMITE_DESCONTO_10:
            valor_final = valor_total * (1 - self.TAXA_DESCONTO_10)
        return round(valor_final, 2)
