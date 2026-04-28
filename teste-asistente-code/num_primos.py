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
