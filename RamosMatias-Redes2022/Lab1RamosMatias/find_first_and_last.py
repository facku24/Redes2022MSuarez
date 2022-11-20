from convert_address import convertir_de


def find_first_and_last(addr, n):
    addr_en_binario = convertir_de(10, "b", addr, ".", 8, "")
    base = addr_en_binario[0:n]
    tail_first = '0'*(31-n) + '1'
    tail_last = '1'*(31-n) + '0'
    first_addr_en_binario = base + tail_first
    last_addr_en_binario = base + tail_last
   
     
    first_addr_en_decimal = convertir_de(2, "d", first_addr_en_binario, "", 0, ".")
    last_addr_en_decimal = convertir_de(2, "d", last_addr_en_binario, "", 0, ".")
    
    error = ''
    return ((first_addr_en_decimal, last_addr_en_decimal), error)





