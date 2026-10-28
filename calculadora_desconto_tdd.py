class CalculadoraDescontoTDD:
    LIMITE_DESCONTO_10 = 500.0
    TAXA_DESCONTO_10 = 0.10
    LIMITE_DESCONTO_20 = 1000.0
    TAXA_DESCONTO_20 = 0.20
    TAXA_DESCONTO_VIP = 0.05

    def calcular_pedido(self, valor_total: float, vip: bool = False) -> float:
        valor_apos_faixa = self._aplicar_desconto_faixa(valor_total)
        valor_apos_vip = self._aplicar_desconto_vip(valor_apos_faixa, vip)
        if valor_apos_vip < 100.0:
            valor_apos_vip += 15.0
        return round(valor_apos_vip, 2)

    def _aplicar_desconto_faixa(self, valor_total: float) -> float:
        if valor_total > self.LIMITE_DESCONTO_20:
            return valor_total * (1 - self.TAXA_DESCONTO_20)
        if valor_total > self.LIMITE_DESCONTO_10:
            return valor_total * (1 - self.TAXA_DESCONTO_10)
        return valor_total

    def _aplicar_desconto_vip(self, valor: float, vip: bool) -> float:
        if vip:
            return valor * (1 - self.TAXA_DESCONTO_VIP)
        return valor
