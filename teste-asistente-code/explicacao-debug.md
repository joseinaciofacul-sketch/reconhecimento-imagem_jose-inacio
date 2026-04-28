# Depuração do código `debug.py`

Este documento descreve os erros encontrados no código original de `debug.py` e as correções aplicadas.

## Erros Identificados e Correções

### 1. Erro de Sintaxe no `input` (Linha 5)
**Erro Original:**
```python
item1 = float(input(Preço do item 1? ))
```
**Problema:** Faltavam aspas duplas no argumento da função `input`. Isso causava um erro de sintaxe porque o Python interpretava `Preço do item 1?` como uma variável indefinida.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```
**Explicação:** Adicionadas aspas duplas para tornar o texto uma string válida.

### 2. Tipo de Dados Incorreto para `desconto_cupom` (Linha 18)
**Erro Original:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```
**Problema:** `input()` retorna uma string, mas o código tentava usar `desconto_cupom` como um número na divisão. Isso causaria um `TypeError` ao executar.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```
**Explicação:** Convertido o resultado do `input` para `float` para permitir operações matemáticas.

### 3. F-String Incorreta (Linha 27)
**Erro Original:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```
**Problema:** Faltava o prefixo `f` antes das aspas para indicar que é uma f-string. Sem isso, o texto era impresso literalmente, sem substituir as variáveis.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```
**Explicação:** Adicionado o prefixo `f` para ativar a interpolação de strings.

### 4. Comparação de Tipos Incompatíveis (Linha 31)
**Erro Original:**
```python
if desconto_cupom > 0:
```
**Problema:** `desconto_cupom` era uma string (antes da correção), e não podia ser comparada diretamente com um número inteiro. Mesmo após a correção para `float`, isso funcionaria, mas era parte do problema de tipo.

**Correção:** Após converter `desconto_cupom` para `float`, a comparação funciona corretamente.

**Explicação:** A correção do tipo resolveu esse problema.

### 5. Formatação de String com Tipo Incorreto (Linha 32)
**Erro Original:**
```python
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Problema:** `desconto_cupom` era uma string, e o formato `.0f` esperava um número. Isso causaria um `ValueError` ao tentar formatar.

**Correção:** Após converter `desconto_cupom` para `float`, a formatação funciona.

**Explicação:** A conversão para `float` permite a formatação numérica.

### 6. Indentação Incorreta (Linha 32)
**Erro Original:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Problema:** A linha do `print` não estava indentada dentro do bloco `if`, causando um `IndentationError`.

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Explicação:** Adicionada indentação de 4 espaços para o bloco `if`.

### 7. Formatação Redundante no Total (Linha 35)
**Erro Original:**
```python
print(f" TOTAL:         R$ {round(total, 2):.2f}")
```
**Problema:** `round(total, 2)` já arredonda para 2 casas decimais, e `.2f` aplica formatação adicional, mas não é um erro crítico.

**Correção:**
```python
print(f" TOTAL:         R$ {total:.2f}")
```
**Explicação:** Removido `round()` pois `.2f` já formata adequadamente, evitando redundância.

## Código Corrigido

O código corrigido está disponível em `debug.py`. Todas as correções foram aplicadas para garantir que o programa execute sem erros e produza a saída esperada.