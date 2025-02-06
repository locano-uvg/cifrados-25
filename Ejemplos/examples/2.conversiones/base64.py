def transformar_a_base_64(numero):
    """
    Transforma un número base 10 a base 64.

    Parámetros:
    numero: int > 0

    Retorna:
    str: representación en base 64 del número
    """
    if numero == 0:
        return '0'
    base_64 = ''
    while numero > 0:
        base_64 = str(numero % 64) + base_64
        numero = numero // 64
    return base_64

def transformar_a_base10(numero):
    """
    Transforma un número a base 10.

    Parámetros:
    numero: str

    Retorna:
    int: representación en base 10 del número
    """
    base_10 = 0
    for i in range(len(numero)):
        base_10 += int(numero[i]) * (64 ** (len(numero) - i - 1))
    return base_10

