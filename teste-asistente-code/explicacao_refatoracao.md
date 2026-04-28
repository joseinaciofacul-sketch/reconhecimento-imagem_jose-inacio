# Explicação do código `refatoracao.py`

Este arquivo descreve linha a linha o comportamento do script `refatoracao.py`.

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

## Explicação linha a linha

- `def c(l):`
  - Define a função `c`, que recebe uma lista `l` de números.

- `t=0`
  - Inicializa a variável `t` com 0. Essa variável será usada para somar todos os valores da lista.

- `for i in range(len(l)):`
  - Inicia um loop que percorre todos os índices da lista `l`, de 0 até `len(l) - 1`.

- `t=t+l[i]`
  - Adiciona o valor do elemento atual da lista à soma total `t`.

- `m=t/len(l)`
  - Calcula a média dos valores da lista dividindo a soma total `t` pelo número de elementos.

- `mx=l[0]`
  - Inicializa `mx` com o primeiro elemento da lista. `mx` vai guardar o maior valor encontrado.

- `mn=l[0]`
  - Inicializa `mn` com o primeiro elemento da lista. `mn` vai guardar o menor valor encontrado.

- `for i in range(len(l)):`
  - Inicia outro loop que percorre todos os índices da lista novamente.

- `if l[i]>mx:`
  - Verifica se o elemento atual é maior que o maior valor armazenado em `mx`.

- `mx=l[i]`
  - Atualiza `mx` quando encontra um valor maior.

- `if l[i]<mn:`
  - Verifica se o elemento atual é menor que o menor valor armazenado em `mn`.

- `mn=l[i]`
  - Atualiza `mn` quando encontra um valor menor.

- `return t,m,mx,mn`
  - Retorna uma tupla com quatro valores: soma total `t`, média `m`, maior valor `mx` e menor valor `mn`.

- `x=[23,7,45,2,67,12,89,34,56,11]`
  - Cria a lista `x` com dez números inteiros para teste.

- `a,b,c2,d=c(x)`
  - Chama a função `c` com a lista `x` e armazena os resultados em quatro variáveis:
    - `a`: soma total
    - `b`: média
    - `c2`: maior valor
    - `d`: menor valor

- `print("total:",a)`
  - Imprime a soma total dos números da lista.

- `print("media:",b)`
  - Imprime a média dos números da lista.

- `print("maior:",c2)`
  - Imprime o maior número encontrado na lista.

- `print("menor:",d)`
  - Imprime o menor número encontrado na lista.
