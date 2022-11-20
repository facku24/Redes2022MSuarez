#!/usr/bin/env python
# encoding: utf-8
"""
Receptor.py
"""
import argparse
import socket
import logging
import Paquete
from pickle import *

logger = logging.getLogger(__name__)


def is_socket_closed(sock: socket.socket) -> bool:
    try:
        # this will try to read bytes without blocking and also without removing them from buffer (peek only)
        data = sock.recv(16, socket.MSG_DONTWAIT | socket.MSG_PEEK)
        if len(data) == 0:
            return True
    except BlockingIOError:
        return False  # socket is open and reading from it would block
    except ConnectionResetError:
        return True  # socket was closed for some other reason
    except OSError:
        return True
    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        return False
    return False


if __name__ == "__main__":
    # -----------------------------------------------------------------
    # LEYENDO ARGUMENTOS
    # -----------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("puertoReceptor", help="Numero de puerto donde escucha el receptor")
    parser.add_argument("--m", help="m para la cantidad de bist a usar en la enumeracion")
    args = parser.parse_args()

    
    m = int(args.m)

    print('#-------------------------------------------------------------------#')
    print('#                       INICIANDO RECEPTOR                          #')
    print('#-------------------------------------------------------------------#')

    puertoReceptor = int(args.puertoReceptor)

    # -----------------------------------------------------------------
    # CREACION DE SOCKET
    # -----------------------------------------------------------------
    rcvrSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rcvrSock.bind(('127.0.0.1', puertoReceptor))
    rcvrSock.listen(1)
    print('Aguardando conexion...')
    rcvrConn, addr = rcvrSock.accept()

    # -----------------------------------------------------------------
    # MAQUINA DE ESTADOS FINITA -- COMPLETAR
    # -----------------------------------------------------------------
    
    espacio_nroSeq = 2**m
    Rn = 0
    Rsize = 2**(m-1)
    #ventana = [('', False), ('', False), ('', False), ('', False)]
    ventana = [('', False) for i in range(0, Rsize)]
    mensaje = ''
    while not is_socket_closed(rcvrConn):
        try:
            print('Esperando mensaje...', end="")
            msg = rcvrConn.recv(1024)
            print('... mensaje recibido: ' + loads(msg).get_datos())
            paquete = loads(msg)
            longitud = paquete.get_longitud()
            checksum = paquete.get_checksum()
            nroSeq = paquete.get_secuencia()
            ack = paquete.get_ack()
            checksum_paquete = Paquete.calcular_checksum_de_paquete(paquete)
            checksum_datos = Paquete.calcular_checksum_de_datos(longitud, checksum, nroSeq, ack)
            if checksum_paquete != 0 or checksum_datos != 0:
                print("es corrupto")
                pass
            elif nroSeq < Rn or nroSeq > Rn + Rsize - 1:
                print("fuera de la ventana")
                pass
            else:
                indice = nroSeq - Rn
                if ventana[indice][1] == True:
                    pass
                else:
                    print("aceptado")
                    datos = paquete.get_datos()
                    ventana[indice] = (datos, True)
                    if nroSeq == Rn:
                        for i in range(0, Rsize):
                            tupla = ventana[i]
                            datos = tupla[0]
                            recibido = tupla[1]
                            if recibido:
                                mensaje += datos
                                Rn = (Rn + 1) % espacio_nroSeq
                                ventana[i] = ('', False)
                            else:
                                break

        except EOFError or OSError:
            print('Cerrando conexion') 
            rcvrConn.close()
    print(mensaje)
    rcvrSock.close()
