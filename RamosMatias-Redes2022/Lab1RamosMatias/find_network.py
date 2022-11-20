"""2. find_network(addr, n):
Args : addr: es un string representando una dirección de red en formato decimal punteado.
n: es un entero representando la máscara de red en notación barra invertida.
Return : (dec, msg), donde dec es la dirección de la red en decimal punteado y msg es el mensaje de
error igual a null si todo sale bien, o bien "Dirección o Mensaje Incorrecto" en el caso de
que de addr sea incorrecto.
"""

def _convertDesdeBinario(addr):
    viejaBase = 2
    nuevaBase = "d"
    separador = ""
    padding = 0
    token = '.'
    
    split_string = []
    lista_de_partes = []
    address = addr
    n = 8
    for i in range(0, len(address), n):
        parte = address[i:i+n]
        lista_de_partes.append(parte)
    split_string = lista_de_partes
    resultado = ''
    for elem in split_string:
        parte_ya_formateada = format(int(elem, viejaBase), nuevaBase).zfill(padding)
        if resultado == '':
            resultado = parte_ya_formateada
        else:
            resultado = resultado + token + parte_ya_formateada
    return resultado

def find_network(addr, n):
    error = ""
    if "." not in addr:
        error = "Dirección o Mensaje Incorrecto"
    mascara = ""
    slash = n #por ej = 16
    for i in range(slash):
        mascara = mascara + "1"
    for i in range(32-slash):
        mascara = mascara + "0"
    mascara_decimal = _convertDesdeBinario(mascara)
    
    
    x = addr.split(".") # 
    y = mascara_decimal.split(".")
    resultado = []
    for j in range(4): # j = 0, 1, 2, 3
        resultado.append(int(x[j]) & int(y[j]))
        
    resultado_final = [str(elem) for elem in resultado]
    direccion_de_red = ".".join(resultado_final)
    return (direccion_de_red, error)



