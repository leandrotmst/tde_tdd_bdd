# TDE - Desenvolvimento Orientado a Testes (TDD) vs. Abordagem Tradicional

## 1. Contexto e Regras de Negócio
O objetivo desta atividade foi implementar o cálculo do valor final de um pedido de e-commerce seguindo duas abordagens diferentes: primeiro a abordagem tradicional (escrevendo o código antes e os testes depois) e, em seguida, aplicando o ciclo do TDD (*Red - Green - Refactor*).

As regras de negócio consideradas foram:
- Compras acima de R$ 500,00 recebem 10% de desconto;
- Compras acima de R$ 1.000,00 recebem 20% de desconto;
- Clientes VIP ganham 5% de desconto adicional sobre o valor já com desconto;
- Se o valor final do pedido (após os descontos) ficar abaixo de R$ 100,00, é cobrada uma taxa fixa de R$ 15,00 de frete;
- Pedidos com valor total zerado ou negativo devem lançar uma exceção de argumento inválido (`ValueError`).

---

## 2. Etapa 1: Abordagem Tradicional (Code First, Test Later)

### 2.1. Tempo gasto e dificuldades encontradas
Nessa primeira etapa, levei cerca de **45 a 50 minutos** entre escrever a classe inicial (`CalculadoraDescontoTradicional`), testar manualmente pelo `main.py`, perceber que algumas regras tinham ficado de fora ou com cálculo incorreto e, por fim, criar o arquivo de testes unitários (`test_calculadora_desconto_tradicional.py`).

As principais dificuldades que senti ao deixar os testes para o final foram:
1. **Erros que passaram despercebidos na primeira versão do código:** Como tentei programar tudo de uma vez olhando para o enunciado, acabei cometendo alguns erros de atenção. Por exemplo, na faixa acima de R$ 1.000,00 eu havia colocado `15%` de desconto em vez de `20%`. Além disso, no cálculo do cliente VIP, minha primeira ideia foi fazer `desconto *= 1.05`, mas depois percebi que isso estava errado: se a compra fosse de R$ 200,00 (onde o desconto inicial é 0%), multiplicar 0 por 1.05 continuava dando zero, sendo que o cliente VIP deveria receber 5% sobre o valor da compra.
2. **Esquecimento de regras secundárias:** Na pressa de fazer o cálculo principal do desconto funcionar junto com a classe `Pessoa` e o `main.py`, acabei esquecendo inicialmente de colocar a regra do frete de R$ 15,00 e a validação de `ValueError` para valores negativos ou zerados, tendo que voltar no código para adicionar depois.
3. **Construtor atrapalhando na hora de criar os testes:** Quando criei a classe pensando apenas no `main.py`, coloquei `preco_original` e `percentual_desconto` como parâmetros obrigatórios no `__init__`. Quando fui criar o `setUp()` dos testes unitários depois, vi que não fazia sentido exigir esses valores na hora de instanciar a calculadora, então precisei ajustar os parâmetros para valores padrão.
4. **Dificuldade para pensar em casos de borda depois que o código já está pronto:** Quando o código já está escrito, a tendência é criar testes só para confirmar que o código funciona nos casos óbvios, em vez de pensar em situações limite (como uma compra de R$ 100,00 de um cliente VIP, que cai para R$ 95,00 após o desconto e, por ficar abaixo de R$ 100,00, passa a somar os R$ 15,00 de frete, fechando em R$ 110,00).

### 2.2. Código desenvolvido na Etapa 1

**Arquivo `calculadora_desconto_tradicional.py`:**
```python
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
```

**Arquivo `test_calculadora_desconto_tradicional.py`:**
```python
import unittest
from calculadora_desconto_tradicional import CalculadoraDescontoTradicional


class TestCalculadoraDescontoTradicional(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraDescontoTradicional()

    def test_compra_sem_desconto_sem_frete(self):
        self.assertEqual(self.calculadora.calcular_compra(2, 100.0, vip=False), 200.00)
        self.assertEqual(self.calculadora.calcular_compra(5, 100.0, vip=False), 500.00)

    def test_compra_acima_de_500_recebe_10_porcento_desconto(self):
        self.assertEqual(self.calculadora.calcular_compra(6, 100.0, vip=False), 540.00)
        self.assertEqual(self.calculadora.calcular_compra(10, 100.0, vip=False), 900.00)

    def test_compra_acima_de_1000_recebe_20_porcento_desconto(self):
        self.assertEqual(self.calculadora.calcular_compra(3, 500.0, vip=False), 1200.00)

    def test_cliente_vip_recebe_5_porcento_adicional_sobre_valor_com_desconto(self):
        self.assertEqual(self.calculadora.calcular_compra(2, 100.0, vip=True), 190.00)
        self.assertEqual(self.calculadora.calcular_compra(6, 100.0, vip=True), 513.00)
        self.assertEqual(self.calculadora.calcular_compra(3, 500.0, vip=True), 1140.00)

    def test_frete_fixo_para_valor_final_inferior_a_100(self):
        self.assertEqual(self.calculadora.calcular_compra(1, 80.0, vip=False), 95.00)
        self.assertEqual(self.calculadora.calcular_compra(1, 100.0, vip=False), 100.00)
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
```

---

## 3. Etapa 2: Abordagem Orientada a Testes (TDD)

Na segunda etapa, criei a classe `CalculadoraDescontoTDD` seguindo passo a passo o ciclo **Red -> Green -> Refactor** para cada uma das 5 regras, fazendo um commit para cada etapa do ciclo.

### 3.1. Histórico de Commits dos Ciclos TDD
- **Ciclo 1 (Regra de 10% acima de R$ 500):**
  - `6710586` - `test(tdd-ciclo1): [RED] adiciona teste falhando para desconto de 10% acima de R$ 500`
  - `7982aab` - `feat(tdd-ciclo1): [GREEN] implementa codigo minimo para desconto de 10% acima de R$ 500`
  - `62c8d2d` - `refactor(tdd-ciclo1): [REFACTOR] extrai constantes e adiciona casos de fronteira para regra 1`
- **Ciclo 2 (Regra de 20% acima de R$ 1.000):**
  - `432ac85` - `test(tdd-ciclo2): [RED] adiciona teste falhando para desconto de 20% acima de R$ 1000`
  - `9bb85bf` - `feat(tdd-ciclo2): [GREEN] implementa codigo minimo para desconto de 20% acima de R$ 1000`
  - `c5794c5` - `refactor(tdd-ciclo2): [REFACTOR] extrai metodo _aplicar_desconto_faixa e casos de fronteira para regra 2`
- **Ciclo 3 (Regra de 5% adicional para cliente VIP):**
  - `3984b0e` - `test(tdd-ciclo3): [RED] adiciona teste falhando para desconto adicional de 5% para cliente VIP`
  - `e776efe` - `feat(tdd-ciclo3): [GREEN] implementa codigo minimo para desconto adicional VIP de 5%`
  - `013df8b` - `refactor(tdd-ciclo3): [REFACTOR] extrai metodo _aplicar_desconto_vip e testa VIP em todas as faixas`
- **Ciclo 4 (Regra de frete de R$ 15 abaixo de R$ 100):**
  - `08ea503` - `test(tdd-ciclo4): [RED] adiciona teste falhando para frete fixo de R$ 15 abaixo de R$ 100`
  - `f95b6a8` - `feat(tdd-ciclo4): [GREEN] implementa codigo minimo para frete fixo de R$ 15 abaixo de R$ 100`
  - `9402fb0` - `refactor(tdd-ciclo4): [REFACTOR] extrai metodo _aplicar_frete e casos de fronteira com VIP`
- **Ciclo 5 (Exceção para valor zerado ou negativo):**
  - `e757fe1` - `test(tdd-ciclo5): [RED] adiciona teste falhando para pedido com valor zerado ou negativo`
  - `175f92b` - `feat(tdd-ciclo5): [GREEN] implementa validacao de argumento invalido para valor <= 0`
  - `71a4265` - `refactor(tdd-ciclo5): [REFACTOR] extrai _validar_valor e adiciona metodo calcular_compra`

### 3.2. Código final desenvolvido na Etapa 2

**Arquivo `calculadora_desconto_tdd.py`:**
```python
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
```

**Arquivo `test_calculadora_desconto_tdd.py`:**
```python
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
```

---

## 4. Análise Reflexiva

### 1) Explique em que momento as atividades de Verificação e de Validação ocorreram na Abordagem Tradicional e na Abordagem TDD.

Na engenharia de software, a **Validação** busca responder se estamos construindo o produto certo (se a regra implementada realmente reflete o que o usuário precisa), enquanto a **Verificação** busca responder se estamos construindo o produto corretamente (se o código funciona conforme a especificação técnica e sem bugs).

Na Abordagem Tradicional, tanto a verificação quanto a validação acabaram ficando concentradas no final do desenvolvimento. Enquanto eu escrevia a `CalculadoraDescontoTradicional`, fiz apenas uma leitura inicial do enunciado e fui programando tudo de uma vez. A validação de fato só aconteceu depois que o código já estava pronto, quando fui montar os casos de teste e percebi que tinha interpretado errado a regra do desconto VIP e esquecido casos específicos. Da mesma forma, a verificação através dos testes unitários só rodou no fim, servindo mais para consertar erros que eu já tinha cometido do que para evitá-los.

Já na Abordagem TDD, essas atividades aconteceram de forma contínua em cada pequeno ciclo:
- A **Validação** ocorreu logo no passo **RED**, antes mesmo de existir código. Ao escrever o teste primeiro (por exemplo, definindo que um pedido de R$ 600,00 para cliente VIP deve retornar R$ 513,00), fui obrigado a entender e validar a regra de negócio antes de pensar em `if/else`.
- A **Verificação** aconteceu imediatamente nos passos **GREEN** e **REFACTOR**. Assim que escrevi o código mínimo para passar no teste, a execução da suíte verificou que a regra funcionava e que eu não havia quebrado nenhuma das regras anteriores. Depois, na refatoração, os testes continuaram verificando se a reorganização dos métodos manteve o comportamento correto.

---

### 2) Como a inversão na ordem de escrita dos testes afeta o papel da verificação estática (análise de requisitos/design) e dinâmica (execução de testes)?

Inverter a ordem — escrevendo o teste antes do código — muda bastante a forma como pensamos no problema:

- **Na verificação estática (análise de requisitos e design):**
  Quando programamos no modelo tradicional, pensamos primeiro em "como implementar" (variáveis, laços, condicionais) e muitas vezes deixamos passar detalhes do requisito ou criamos métodos difíceis de chamar depois (como aconteceu no meu construtor da Etapa 1). No TDD, escrever o teste primeiro funciona como uma análise de requisitos e de design antecipada: antes de existir a classe, eu já precisei decidir qual seria o nome do método, quais parâmetros faziam sentido receber (`calcular_pedido(valor_total, vip)`) e o que deveria acontecer nos limites (ex.: exatamente R$ 500,00 vs R$ 500,01). Além disso, a etapa de *Refactor* incentivou a separar cada regra em métodos pequenos e fáceis de ler (`_aplicar_desconto_faixa`, `_aplicar_desconto_vip`, `_aplicar_frete`).

- **Na verificação dinâmica (execução dos testes):**
  Na abordagem tradicional, como escrevemos o teste para um código que já está pronto, o teste já nasce passando. Isso traz o perigo de escrevermos um teste fraco ou viciado no código existente sem perceber. No TDD, a verificação dinâmica começa vendo o teste **falhar** (passo *Red*), o que garante que o teste realmente está testando aquela regra. Além disso, a execução dos testes deixa de ser uma etapa pesada de caça a bugs no final do projeto e passa a dar feedback rápido a cada mudança: se algum teste falha, sabemos que o problema está nas poucas linhas que acabamos de mexer.
