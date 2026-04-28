# Explicação do código `num_primos.py`

Este arquivo descreve linha a linha a função `eh_primo` e o bloco principal do script.

```python
def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, caso contrário False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


if __name__ == "__main__":
    exemplos = [1, 2, 3, 4, 17, 18, 19, 20, 97]
    for numero in exemplos:
        resultado = eh_primo(numero)
        print(f"{numero} é primo? {resultado}")
```

## Explicação linha a linha

- `def eh_primo(n: int) -> bool:`
  - Declara a função `eh_primo`, que recebe um inteiro `n` e retorna um valor booleano (`True` ou `False`).

- `"""Retorna True se n for primo, caso contrário False."""`
  - Documentação da função, explicando o propósito do código.

- `if n <= 1:`
  - Verifica se `n` é menor ou igual a 1. Números 1 e negativos não são primos.

- `return False`
  - Retorna `False` para valores que não podem ser primos.

- `if n <= 3:`
  - Verifica se `n` é 2 ou 3. Esses valores são primos.

- `return True`
  - Retorna `True` para 2 e 3.

- `if n % 2 == 0 or n % 3 == 0:`
  - Verifica se `n` é divisível por 2 ou por 3. Se for, não é primo (exceto 2 e 3, que já foram tratados).

- `return False`
  - Retorna `False` quando `n` é divisível por 2 ou 3.

- `i = 5`
  - Inicializa `i` com 5 para começar os testes de divisibilidade a partir de 5.

- `while i * i <= n:`
  - Executa o loop enquanto `i` for menor ou igual à raiz quadrada de `n`. Isso é suficiente para encontrar divisores.

- `if n % i == 0 or n % (i + 2) == 0:`
  - Verifica se `n` é divisível por `i` ou por `i + 2`.
  - O loop testa apenas números da forma 6k-1 e 6k+1, que são os candidatos possíveis após eliminar múltiplos de 2 e 3.

- `return False`
  - Retorna `False` se for encontrado um divisor.

- `i += 6`
  - Avança `i` para o próximo par de candidatos (por exemplo, de 5 para 11, depois para 17, etc.).

- `return True`
  - Se nenhum divisor for encontrado até a raiz quadrada de `n`, `n` é primo.

- `if __name__ == "__main__":`
  - Garante que o código a seguir execute apenas quando o arquivo for executado diretamente, e não quando for importado como módulo.

- `exemplos = [1, 2, 3, 4, 17, 18, 19, 20, 97]`
  - Define uma lista de números para testar a função.

- `for numero in exemplos:`
  - Inicia um loop para testar cada número da lista.

- `resultado = eh_primo(numero)`
  - Chama a função `eh_primo` para verificar se o número atual é primo.

- `print(f"{numero} é primo? {resultado}")`
  - Imprime o resultado do teste para cada número.
