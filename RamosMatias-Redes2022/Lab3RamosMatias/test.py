from pickle import *
import socket
import Paquete 
import time
import argparse

# -----------------------------------------------------------------
# LEYENDO ARGUMENTOS
# -----------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("puertoReceptor", help="Numero de puerto donde escucha el receptor")
args = parser.parse_args()

puertoReceptor = 22001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', int(args.puertoReceptor)))

#---------------------------------------------------------
#       PRIMER ENVIO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('uno ', 1, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('dos ', 2, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       Paquete FUERA DE VENTANA
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cero ', 6, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

time.sleep(1)
p = Paquete.Paquete('tres ', 3, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('cero ', 0, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       Paquete CORRUPTO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cero ', 0, 0)
p.set_checksum(12)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       SEGUNDO ENVIO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cinco ', 5, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('seis ', 6, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('siete ', 7, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('cuatro ', 4, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       PAQUETE CORRUPTO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cero ', 0, 0)
p.set_checksum(12)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       Paquete FUERA DE VENTANA
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cero ', 6, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       TERCER ENVIO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('nueve ', 1, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('diez ', 2, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('once ', 3, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('ocho ', 0, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       Paquete CORRUPTO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cero ', 0, 0)
p.set_checksum(12)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       Paquete FUERA DE VENTANA
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('cero ', 2, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

#---------------------------------------------------------
#       CUARTO ENVIO
#---------------------------------------------------------
time.sleep(1)
p = Paquete.Paquete('trece ', 5, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('catorce ', 6, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('quince ', 7, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))
time.sleep(1)
p = Paquete.Paquete('doce ', 4, 0)
print('Enviando mensaje: ' +  p.get_datos())
sock.send(dumps(p))

sock.close()