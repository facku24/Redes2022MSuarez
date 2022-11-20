"""Args : addr es un string representando una dirección de red en cualquiera de los tres posibles for-
matos, decimal punteado, binario o hexadecimal.
Return : ((dec, bin, hex), msg), donde la terna se conforma por las dirección en los tres formatos
existentes y msg es el mensaje de error igual a nil si todo sale bien, o bien "Dirección o
Mensaje Incorrecto" en el caso de que de addr sea incorrecto
"""

def convertir_de(viejaBase, nuevaBase, addr, separador, padding, token):
    split_string = [] 
    if separador == "":
        lista_de_partes = []
        address = addr
        n = 8
        for i in range(0, len(address), n): 
            parte = address[i:i+n]
            lista_de_partes.append(parte)
        split_string = lista_de_partes
    elif separador == ".":
        decimal = addr   
        split_string = (decimal.split("."))
    elif separador == ":":
        hexadecimal = addr
        split_string = (hexadecimal.split(":"))
    resultado = ''
    for elem in split_string[0:]: 
        parte_ya_formateada = format(int(elem, viejaBase), nuevaBase).zfill(padding)
        if resultado == '': 
        	resultado = parte_ya_formateada
        else:
            resultado = resultado + token + parte_ya_formateada
    return resultado


def convert_address(addr):
	
    def convertDesdeDecimal(addr): 
        bin_adres = convertir_de(10,"b",addr,".",8, '')
        hex_adres = convertir_de(10,"x",addr,".",2, ':')   
        return (bin_adres,addr,hex_adres)
    
    
    def convertDesdeBinario(addr):
        dec_adres = convertir_de(2,"d",addr,"",0, '.')
        hex_adres = convertir_de(2,"x",addr,"",2, ':')
        return (addr,dec_adres,hex_adres)
    
    
    def convertDesdeHexadecimal(addr):
        dec_adres = convertir_de(16,"d",addr,":",0, '.')
        bin_adres = convertir_de(16,"b",addr,":",8, '')
        return (bin_adres,dec_adres,addr)


    error = ''
    if "." in addr: 
        binario,decimal,hexadecimal = convertDesdeDecimal(addr)
        return ((binario,decimal,hexadecimal), error)
    elif ":" in addr:
        binario,decimal,hexadecimal = convertDesdeHexadecimal(addr)
        return ((binario,decimal,hexadecimal), error)
    elif len(addr) == 32: 
        binario,decimal,hexadecimal = convertDesdeBinario(addr)
        return ((binario,decimal,hexadecimal), error)
    else:
        error =  ((), "Dirección o Mensaje Incorrecto")







