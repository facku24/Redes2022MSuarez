import math

class Paquete:
    def __init__(self, datos, secuencia, ack):
        self.checksum   = calcular_checksum_de_datos(len(datos) + 8, 0, secuencia, ack)
        self.longitud   = len(datos) + 8
        self.datos      = datos
        self.secuencia  = secuencia
        self.ack        = ack


    def set_checksum(self, new_checksum):
        self.checksum = new_checksum


    def get_direccion(self):
        return (self.direccion, self.puerto)


    def get_longitud(self):
        return self.longitud


    def get_checksum(self):
        return self.checksum


    def get_datos(self):
        return self.datos


    def get_secuencia(self):
        return self.secuencia


    def get_ack(self):
        return self.ack


def complemento_uno(number):
    num_bits = int(math.log2(number)) + 1
    complemento = ((0b1 << num_bits) - 1) ^ number
    return complemento


def calcular_checksum_de_paquete(packet):
    sum_aux = packet.get_checksum() + packet.get_longitud()
    sum_aux += packet.get_secuencia() + packet.get_ack()
    resultado = complemento_uno(sum_aux)
    return resultado


def calcular_checksum_de_datos(longitud, checksum, secuencia, ack):
    sum_aux = longitud + checksum + secuencia + ack
    resultado = complemento_uno(sum_aux)
    return resultado
