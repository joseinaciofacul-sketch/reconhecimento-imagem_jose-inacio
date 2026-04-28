from typing import Iterable, Tuple


def calcular_estatisticas(numeros: Iterable[float]) -> Tuple[float, float, float, float]:
    """Retorna a soma, média, maior e menor valor de uma sequência de números."""
    numeros_lista = list(numeros)
    if not numeros_lista:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(numeros_lista)
    media = total / len(numeros_lista)
    maior = max(numeros_lista)
    menor = min(numeros_lista)

    return total, media, maior, menor

if __name__ == "__main__":
    valores = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    soma, media, maior_valor, menor_valor = calcular_estatisticas(valores)

    print("total:", soma)
    print("media:", media)
    print("maior:", maior_valor)
    print("menor:", menor_valor)