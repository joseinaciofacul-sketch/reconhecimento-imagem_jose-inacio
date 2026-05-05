def eh_primo(n: int) -> bool:
    """Verifica se um número é primo.

    Args:
        n (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
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
