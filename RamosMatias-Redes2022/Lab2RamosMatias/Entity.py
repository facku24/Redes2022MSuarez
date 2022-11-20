from Constantes import *
from Packet import *

class Entity:

    def __init__(self, nro_nodo, simulacion):
        self.nro_nodo = nro_nodo
        self.simulacion   = simulacion
        self.numero_entidades = self.simulacion.numero_entidades()
        self.__distanceTable = [[0] * self.numero_entidades for i in range(self.numero_entidades)]
        self.D = [0 for i in range(self.numero_entidades)]

        for y in range(self.numero_entidades):
            if y == self.nro_nodo:
                pass
            costo_hacia_y = self.simulacion.get_cost(self.nro_nodo, y) 
            if costo_hacia_y != 999: 
                self.D[y] = costo_hacia_y
            else: 
                self.D[y] = 999
        for y in range(self.numero_entidades):
            if y == self.nro_nodo: 
                pass
            costo_hacia_y = self.simulacion.get_cost(self.nro_nodo, y)
            if costo_hacia_y != 999: 
                fuente = self.nro_nodo
                destino = y 
                vector_de_distancias = self.D
                paquete: Packet = Packet(fuente, destino, vector_de_distancias)
                self.simulacion.to_layer_2(paquete)
            else:
                pass

    def update(self, p:Packet) -> None:
        w = p.get_source() 
        el_costo_hacia_w = self.simulacion.get_cost(self.nro_nodo, w)
        hubo_algun_cambio = False
        for y in range(self.numero_entidades): 
            if y == self.nro_nodo: 
                pass
            if y == w:
                pass
            el_costo_de_w_hacia_y = p.get_min_cost(y) 
            nuevo_costo_posible = el_costo_hacia_w + el_costo_de_w_hacia_y
            el_costo_anterior = self.D[y]
            if nuevo_costo_posible < el_costo_anterior:
                self.D[y] = nuevo_costo_posible
                hubo_algun_cambio = True
            else: 
                pass
        if hubo_algun_cambio:
            for y in range(self.numero_entidades): 
                if y == self.nro_nodo:
                    continue
                costo = self.simulacion.get_cost(self.nro_nodo, y)
                if costo != 999: 
                    fuente = self.nro_nodo
                    destino = y
                    vector_de_distancias = self.D
                    paquete: Packet = Packet(fuente, destino, vector_de_distancias)
                    self.simulacion.to_layer_2(paquete)
                else:
                    pass

    def link_cost_change_handler(self, which_link:int, new_cost:int) -> None:
        pass


    def obtener_tabla(self):
        return self.D
