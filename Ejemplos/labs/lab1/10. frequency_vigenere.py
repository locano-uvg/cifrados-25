
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
# https://inventwithpython.com/hacking/chapter21.html


# OBTENER FRECUENCIAS DE LETRAS
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

    # Calcular la frecuencia relativa
    total_caracteres = sum(frecuencias.values())
    frecuencia_relativa = {letra: frecuencia / total_caracteres for letra, frecuencia in frecuencias.items()}

    return frecuencia_relativa

def calcular_frecuencia_de_textos(textos_cifrados):
    frecuencias_textos = []
    for texto in textos_cifrados:
        nueva_frecuencia = calcular_frecuencia(texto)
        nueva_frecuencia = sorted(nueva_frecuencia.items(), key=lambda x: x[1], reverse=True)
        frecuencias_textos.append(nueva_frecuencia)

    #ORDERNAR FRECUENCIAS
    return frecuencias_textos

# -------------------------------------------------

# DIVIDIR TEXTO EN NUEVOS ARREGLOS DEPENDIENDO DE LA LONGITUD DE LA CLAVE
def dividir_texto(texto_cifrado, n):
    arreglo_textos = [""] * n
    nuevo_texto = ""
    contador = 0

    for i in range(0,len(texto_cifrado)):
        arreglo_textos[contador] += texto_cifrado[i]
        if contador == 3:
            contador = 0
        else:
            contador += 1
    return arreglo_textos


# -------------------------------------------------

# CONTAR LAS LETRAS IGUALES ENTRE DOS TEXTOS
def contar_letras_iguales(texto,texto_cifrado):
    # Inicializar el diccionario de frecuencias
    frecuencias = 0
    for index in range(0,len(texto_cifrado)):
        frecuencias += 1 if texto_cifrado[index] == texto[index] else 0
    return frecuencias

# OBTENER REPETICIONES DE LETRAS
def obtener_repeticiones_letras(texto_cifrado):
    repeticiones = {}
    for movimiento in range(1,len(texto_cifrado)):
        # llenar de espacios un texto desde una posicion hasta el final
        nuevo_texto = " " * movimiento
        nuevo_texto += texto_cifrado[:len(texto_cifrado)-movimiento]
        repeticiones[movimiento] = contar_letras_iguales(nuevo_texto,texto_cifrado)

    # obtener longitud de la clave
    longitud_clave = 0
    index_longitud = 0
    for key in range(1,len(repeticiones)):
        if repeticiones[key] > longitud_clave:
            longitud_clave = repeticiones[key]
        else:
            index_longitud  = key - 1
            break

    return index_longitud
    


def descifrar_vigenere(texto, clave):
    m = len(alfabeto)

    # Convertir el texto cifrado y la clave a minúsculas para evitar problemas con mayúsculas
    texto_cifrado = texto.lower()
    clave = clave.lower()

    texto_descifrado = ""
    clave_extendida = ""
    if len(clave) < len(texto):
        # Extender la clave para que tenga la misma longitud que el texto
        for i in range(len(texto)):
            clave_extendida += clave[i % len(clave)]
    else:
        clave_extendida = clave[:len(texto)]

    for caracter_cifrado, clave_caracter in zip(texto_cifrado, clave_extendida):
        if caracter_cifrado.isalpha():
            es_mayuscula = caracter_cifrado.isupper()
            caracter_cifrado = caracter_cifrado.lower()
            clave_caracter = clave_caracter.lower()

            # Calcular la posición descifrada
            posicion_descifrado = (alfabeto.index(caracter_cifrado) - alfabeto.index(clave_caracter)) % m

            # Obtener el caracter descifrado
            caracter_descifrado = alfabeto[posicion_descifrado]

            # Mantener la mayúscula si el caracter cifrado es mayúscula
            if es_mayuscula:
                caracter_descifrado = caracter_descifrado.upper()

            texto_descifrado += caracter_descifrado
        else:
            texto_descifrado += caracter_cifrado

    return texto_descifrado





# Ejemplo de uso:
texto_cifrado = "DYEFESJKBCFSSXSDPPISSVERPOELFWMFUMSIFVHAESEUFTXHRYIQBQEVBTSVSMELBOZSSOSDBWIDWETHEIVHTEHWHYEMFPEDBOSZBFMSBTVWTEHHJPTDBGETMICVFJMFJXMÑBEQMFWYAHQSKBQGABXSIPKVSGMGSTIWWÑXSUPQXKBQUNJOMVBHEWTTIKBVOSNYIKUIUNJWSEPVMKBOOATMQFJQKNÑEILQIVSÑDESJWOSESGHÑIOIFQWSNMIFUSJAKSIFMEILQERSEMWMBQXWQEVMJGYDBVPWÑXIWÑIOUPQZWÑXSVFOSLBFVHKSWVPQHWDEVDPWUNJQXHDSQVFWGWÑHMWSEYFBZIRBFEBBVHWTYIEJQIFDMEIBVEVFGMKMIUNFGSFGMETBIQWMGIDPVIDJKMHTSHWTYOSCSVKFHIFUSVSBOHWTTIKUEVLFIQUPQXKPVSVFEHHQSVNÑKVNQSHWJQHAHIQSTHIKPWXKPMPIBWMTMIUNFWIVJWTHÑMEFBWEUSMJADEVDPEQMFYQSMXEKVQEDUEVJVIETBVXHMSPWMITSSIGAPGSEPIODFGLHFQUNFHILDEQLBVMSBOJAÑHILVWXWNSVWTHILVHILUMQHEIWANMWEPXVWTERHTIQWMTEATOIZBFMSÑGSFGIVAESYFNIHABQSVPPMFJSHWMEWDFQKNBWQSUMZSTMQMFQXHBOKHEMNHBOKNÑEWIBOETSEWJVIJNFVSFDSPISIQVJHELFQXHÑGILGOSKFGMHFQIDVQEAEIEJVIXNWSTHSHMYÑEHWTYXSMIQMPCHWTYGNMXYKBYQAWIVLBOCVFWYSSHYHDSQHDMPAFQXHEIEKJWXHUIOWTVIUPVHHRYIIBVEWTIHABWIWTTIKBFENÑIGDJTWWUSXSMHILPOCVJWTNTSIFMSPSTMQMJPSÑBOIKTIHWBUYWMGSFPGMEJIQMPTEKBIQYBREKBWYLPTVWTSVWTCWSMZEKMEZAEEWANIPSUEMLMIWVJNSIVIHHIEGWSUYWFOWHMWIHTGYKFDGSFQWNBOXNSEOHTMQVJKIFBWOHNMVSSSQXJNEEFQXWZFEKUSOHNIWHSTVWÑHMHMEMFDVIVVOMVBHIFTYWHKSWÑJSUNFWIISSHNKSYFQIUNFRSUPQWWKSCWTTIKPGSFGMEVPQSLJQGAFVXHEIWVFQHHTLSKBWHWTTYWTIOUPVERPQHWGVEQCEVMPOSEFEVKBDSDBGLHSVISCEWNTEQYSIZWIIPWÑXILPFVWMETAFHVSEIOHTWEUSMJADMSLCVMDMEQMFFEBPOEHQEGSMYDVFYQLPOIUMMTLBHSEJIQMSEWNÑSHWMSWAÑHMYFQELSIGAUEFSTMQFJQKNÑEMFGOIPJSQVFZSRTMQISMWSVQEIPVYFBOELJQJAÑMXSTJIUIEWWÑUYWTITKPHYUJVMSÑIGDJTWWTWSDBVILZOYFBVILRYIDPWELUVSFPPSLEIOSDSPNÑMHSEPEQBLETJEQISIZATXSQBQSMBHSWÑWYLDSHADIWLJQOSWEOAPWESZYHSEIEKJWXHUIOWT"
# clave = input("Introduce la clave: ")
longitud_clave = obtener_repeticiones_letras(texto_cifrado)
nuevo_grupo_textos = dividir_texto(texto_cifrado, longitud_clave)
calcular_frecuencia_de_textos(nuevo_grupo_textos)

# texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
# print("Texto descifrado:", texto_descifrado)