Você foi contratado para implementar o módulo central de um Sistema de Cobrança e Descontos de um E-commerce. O módulo possui as seguintes regras de negócio:

## Calculo do Valor Final do Pedido:
    Compras acima de R$ 500,00 recebem 10% de desconto.
    Compras acima de R$ 1.000,00 recebem 20% de desconto.
    Clientes da categoria VIP ganham 5% de desconto adicional sobre o valor já com desconto.
    Se o valor final do pedido (após descontos) for inferior a R$ 100,00, é cobrada uma taxa fixada de frete de R$ 15,00.
    Pedidos com valor total de itens zerado ou negativo devem lançar uma exceção de argumento inválido.

A atividade está dividida em duas etapas práticas de desenvolvimento e uma etapa final de análise reflexiva.

## Etapa 1: Abordagem Tradicional (Code First, Test Later)
    1. Crie uma classe/módulo no seu projeto chamada CalculadoraDescontoTradicional.
    2. Implemente primeiro toda a lógica de código necessária para atender a todas as regras de negócio descritas no contexto.
    3. Apenas após finalizar o código, crie uma suíte de testes unitários para verificar se a sua implementação atende aos requisitos.
    4. Anote o tempo gasto e as dificuldades encontradas ao escrever os testes para um código já pronto.

## Etapa 2: Abordagem Orientada a Testes (TDD - Test Driven Development)
    1. Crie uma classe/módulo no seu projeto chamada CalculadoraDescontoTDD.
    2. Aplique rigorosamente o ciclo abaixo:
        * Escreva um teste unitário que falhe para a primeira regra de negócio.
        * Escreva o código mínimo necessário para fazer o teste passar.
        * Melhore o código e os testes garantindo que tudo continue passando.
    3. Repita o ciclo passo a passo para cada uma das regras de negócio.
    4. Mantenha os históricos de commits no Git registrados a cada passo do ciclo.

Após concluir o desenvolvimento das duas abordagens, elabore um documento contendo todos os artefatos desenvolvidos e respondendo às seguintes questões:
    * Explique em que momento as atividades de Verificação e de Validação ocorreram na Abordagem Tradicional e na Abordagem TDD.
    * Como a inversão na ordem de escrita dos testes afeta o papel da verificação estática (análise de requisitos/design) e dinâmica (execução de testes)?