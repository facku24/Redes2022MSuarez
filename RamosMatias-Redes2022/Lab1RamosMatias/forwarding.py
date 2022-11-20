from convert_address import convertir_de

def forwarding(forw_table, addr):
    for entrada in forw_table:
        dir_red_slash = entrada[0]
        interfaz = entrada[1]
        dir_red_decimal = dir_red_slash[0]
        slash = dir_red_slash[1]
        address_binario = convertir_de(10, "b", addr, '.', 8, '')
        primera_parte = address_binario[0:slash]
        segunda_parte = (32-slash)*'0'
        address_slasheada = primera_parte + segunda_parte
        address_slasheada_decimal = convertir_de(2, "d", address_slasheada, '', 0, '.')
        if address_slasheada_decimal == dir_red_decimal:
            return interfaz

    ultima_posicion_fowr_table = len(forw_table)-1
    ultima_entrada = forw_table[ultima_posicion_fowr_table]
    interfaz = ultima_entrada[1]
    return interfaz
    
