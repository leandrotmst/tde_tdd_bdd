from calculadora_desconto_tradicional import CalculadoraDescontoTradicional
from pessoa import Pessoa


def main():
    preco_original = float(input("Digite o preço unitário do produto: "))
    quantidade = int(input("Digite a quantidade de itens: "))
    nome_cliente = input("Digite o nome do cliente: ")
    vip_input = input("O cliente é VIP? (s/n): ").strip().lower()
    vip = vip_input == "s"

    pessoa = Pessoa(nome_cliente, vip)
    calculadora = CalculadoraDescontoTradicional(preco_original, 0.0)
    preco_final = calculadora.calcular_compra(quantidade, preco_original, pessoa.vip)

    print(f"Preço final para {pessoa.nome}: R$ {preco_final:.2f}")


if __name__ == "__main__":
    main()
