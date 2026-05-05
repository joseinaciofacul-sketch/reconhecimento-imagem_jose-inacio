# Projeto de Exemplos em Python

Este projeto contém exemplos simples de scripts em Python acompanhados de explicações e refatorações. Os arquivos demonstram operações básicas como validação de números primos, cálculos de estatísticas e um pequeno caixa de vendas com desconto.

## Estrutura do projeto

- `debug.py` - Script interativo que calcula o total de uma compra com três itens, adiciona imposto de 10% e aplica um desconto percentual quando há cupom.
- `num_primos.py` - Função que verifica se um número é primo usando uma técnica otimizada e testa vários exemplos quando executado como script.
- `refatoracao.py` - Exemplo de cálculo de soma, média, maior e menor valor a partir de uma lista de números.
- `esplicacao_num_primo.md` - Explicação detalhada do funcionamento do código `num_primos.py`.
- `explicacao-debug.md` - Análise de erros encontrados no código original de `debug.py` e as correções aplicadas.
- `explicacao_refatoracao.md` - Descrição do comportamento do script `refatoracao.py` e sua lógica passo a passo.

## Como executar

1. Abra um terminal no diretório `teste-asistente-code`.
2. Execute os scripts com o Python instalado:

```bash
python debug.py
python num_primos.py
python refatoracao.py
```

### Uso rápido de cada script

- `debug.py`
  - Solicita nome do cliente, quantidade e preço de três itens.
  - Calcula subtotal, aplica imposto de 10% e desconta o valor do cupom informado.
  - Mostra o relatório formatado na tela.

- `num_primos.py`
  - Contém a função `eh_primo(n)` que verifica se `n` é primo.
  - Executa testes com uma lista de números de exemplo e imprime se cada um é primo ou não.

- `refatoracao.py`
  - Define `calcular_estatisticas(numeros)` para retornar soma, média, maior e menor valor.
  - Testa a função com uma lista fixa de valores e mostra os resultados.

## Notas importantes

- O script `debug.py` aceita cupom de desconto em percentual. Se o usuário digitar `0`, o desconto não é exibido.
- O cálculo de primos em `num_primos.py` usa otimização com checagem de divisibilidade por 2 e 3 e depois testa apenas candidatos na forma `6k ± 1`.
- `refatoracao.py` envolve tratamento de lista vazia e lança `ValueError` caso não haja dados.

## Melhorias possíveis

- Adicionar validação de entradas em `debug.py` para evitar valores negativos ou entradas inválidas.
- Criar funções reutilizáveis em `debug.py` para separar entrada, cálculo e exibição.
- Incluir testes automatizados para `num_primos.py` e `refatoracao.py`.

## Licença

Este projeto é um conjunto de exemplos de aprendizado. Sinta-se à vontade para adaptar e expandir os scripts.
