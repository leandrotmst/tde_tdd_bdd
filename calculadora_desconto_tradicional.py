class CalculadoraDescontoTradicional:
    def __init__(self, preco_original: float = 0.0, percentual_desconto: float = 0.0):
        self.preco_original = preco_original
        self.percentual_desconto = percentual_desconto

    def calcular_compra(self, quantidade: int, preco: float, vip: bool = False) -> float:
        if quantidade <= 0 or preco <= 0:
            raise ValueError("Pedidos com valor total de itens zerado ou negativo são inválidos.")

        total = quantidade * preco
        if total > 500 and total <= 1000:
            desconto = 10  # 10% de desconto para compras acima de R$ 500,00 até R$ 1.000,00
        elif total > 1000:
            desconto = 20  # 20% de desconto para compras acima de R$ 1.000,00
        else:
            desconto = 0  # Sem desconto para compras até R$ 500,00

        preco_com_desconto = self._calcular_preco_com_desconto(total, desconto, vip)
        preco_final = self._aplicar_frete(preco_com_desconto)
        return round(preco_final, 2)

    def _calcular_preco_com_desconto(self, total: float, desconto: float, vip: bool = False) -> float:
        valor_desconto = total * (desconto / 100)
        preco_com_desconto = total - valor_desconto
        if vip:
            # Clientes VIP ganham 5% de desconto adicional sobre o valor já com desconto
            preco_com_desconto *= 0.95
        return preco_com_desconto

    def _aplicar_frete(self, valor_apos_descontos: float) -> float:
        # Se o valor final do pedido (após descontos) for inferior a R$ 100,00, cobra frete fixo de R$ 15,00
        if valor_apos_descontos < 100:
            return valor_apos_descontos + 15.0
        return valor_apos_descontos
