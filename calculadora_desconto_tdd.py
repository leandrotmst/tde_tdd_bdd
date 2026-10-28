class CalculadoraDescontoTDD:
    def calcular_pedido(self, valor_total: float, vip: bool = False) -> float:
        if valor_total > 500:
            return valor_total * 0.90
        return valor_total
