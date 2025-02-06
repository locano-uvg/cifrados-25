def calcular_frecuencia(texto_cifrado):
    # Inicializar un diccionario para almacenar las frecuencias
    frecuencias = {}

    # Recorrer cada caracter en el texto cifrado
    for caracter in texto_cifrado:
        # Verificar si el caracter es una letra
        if caracter.isalpha():
            # Convertir a minúsculas para evitar distinción entre mayúsculas y minúsculas
            caracter = caracter.lower()

            # Incrementar la frecuencia del caracter en el diccionario
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
        else:
            frecuencias[caracter] = 0

    # Calcular la frecuencia relativa
    total_caracteres = sum(frecuencias.values())
    frecuencia_relativa = {
        letra: frecuencia / total_caracteres
        for letra, frecuencia in frecuencias.items()
    }

    return frecuencia_relativa


# Ejemplo de uso:
# texto_cifrado = "hqxqoxjdughodpdqfkdghfx|rqrpeuhqrtxlhurdfrugduphylyldxqorfrpdfduudtxhwrfdedodjxlwduud"
# texto_cifrado = "WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW".lower()
texto_cifrado = input("Introduce el texto cifrado: ").lower()
frecuencias = calcular_frecuencia(texto_cifrado)
print("Frecuencia de letras:", frecuencias)



def descifrar_cesar_fuerza_bruta(texto_cifrado):
    try:
        # Calcular la frecuencia de letras en el texto cifrado
        frecuencias_cifrado = calcular_frecuencia(texto_cifrado)

        # Encontrar la letra más frecuente en el cifrado y su posición en el alfabeto
        letra_mas_frecuente = max(frecuencias_cifrado, key=frecuencias_cifrado.get)
        orden_letra_mas_frecuente = ord(letra_mas_frecuente)
        orden_letra_a = ord("a")

        # Buscamos la longitud entre la letra a y la letra más frecuente
        posicion_letra_mas_frecuente = orden_letra_mas_frecuente - orden_letra_a

        # Intentar descifrar el texto para diferentes desplazamientos (fuerza bruta)
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        for desplazamiento_descifrado in range(26):
            texto_descifrado = ""
            for caracter in texto_cifrado:
                if caracter.isalpha():
                    es_mayuscula = caracter.isupper()
                    caracter = caracter.lower()
                    posicion = (
                        alfabeto.index(caracter) - desplazamiento_descifrado
                    ) % 26
                    letra_descifrada = alfabeto[posicion]
                    if es_mayuscula:
                        letra_descifrada = letra_descifrada.upper()
                    texto_descifrado += letra_descifrada
                else:
                    texto_descifrado += caracter

            # Imprimir los resultados para cada desplazamiento
            print(f"Desplazamiento {desplazamiento_descifrado}: {texto_descifrado}")
            print(f"------------------------------------------------")
    except Exception as err:
        print("error:", err)


descifrar_cesar_fuerza_bruta(texto_cifrado)
