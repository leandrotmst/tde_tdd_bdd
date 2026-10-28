class CalculadoraDescontoTDD:
    LIMITE_DESCONTO_10 = 500.0
    TAXA_DESCONTO_10 = 0.10
    LIMITE_DESCONTO_20 = 1000.0
    TAXA_DESCONTO_20 = 0.20
    TAXA_DESCONTO_VIP = 0.05
    LIMITE_ISENCAO_FRETE = 100.0
    TAXA_FRETE = 15.0

    def calcular_pedido(self, valor_total: float, vip: bool = False) -> float:
        self._validar_valor(valor_total)
        valor_apos_faixa = self._aplicar_desconto_faixa(valor_total)
        valor_apos_vip = self._aplicar_desconto_vip(valor_apos_faixa, vip)
        valor_final = self._aplicar_frete(valor_apos_vip)
        return round(valor_final, 2)

    def calcular_compra(self, quantidade: int, preco: float, vip: bool = False) -> float:
        if quantidade <= 0 or preco <= 0:
            raise ValueError("Pedidos com valor total de itens zerado ou negativo são inválidos.")
        return self.calcular_pedido(quantidade * preco, vip=vip)

    def _validar_valor(self, valor_total: float) -> None:
        if valor_total <= 0:
            raise ValueError("Pedidos com valor total de itens zerado ou negativo são inválidos.")

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

    def _aplicar_frete(self, valor_apos_descontos: float) -> float:
        if valor_apos_descontos < self.LIMITE_ISENCAO_FRETE:
            return valor_apos_descontos + self.TAXA_FRETE
        return valor_apos_descontos
