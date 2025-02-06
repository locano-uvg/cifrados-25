def transformar_a_binario(numero):
    """
    Transforma un número base 10 a binario.

    Parámetros:
    numero: int > 0

    Retorna:
    str: representación en binario del número
    """
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

def transformar_a_base10(binario):
    """
    Transforma un número binario a base 10.

    Parámetros:
    binario: str

    Retorna:
    int: representación en base 10 del número
    """
    base_10 = 0
    for i in range(len(binario)):
        base_10 += int(binario[i]) * (2 ** (len(binario) - i - 1))
    return base_10

binario = transformar_a_binario(21)
print(binario)
base10 = transformar_a_base10(binario)
print(base10)
