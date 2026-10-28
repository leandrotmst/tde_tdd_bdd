class CalculadoraDescontoTDD:
    LIMITE_DESCONTO_10 = 500.0
    TAXA_DESCONTO_10 = 0.10
    LIMITE_DESCONTO_20 = 1000.0
    TAXA_DESCONTO_20 = 0.20

    def calcular_pedido(self, valor_total: float, vip: bool = False) -> float:
        valor_final = self._aplicar_desconto_faixa(valor_total)
        if vip:
            valor_final *= 0.95
        return round(valor_final, 2)

    def _aplicar_desconto_faixa(self, valor_total: float) -> float:
        if valor_total > self.LIMITE_DESCONTO_20:
            return valor_total * (1 - self.TAXA_DESCONTO_20)
        if valor_total > self.LIMITE_DESCONTO_10:
            return valor_total * (1 - self.TAXA_DESCONTO_10)
        return valor_total
