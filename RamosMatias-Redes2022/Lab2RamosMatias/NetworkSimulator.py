from random import random
from random import seed
from EventListImpl import *
from Entity import *
import Packet
from Event import *

class NetworkSimulator:
	# Parametros de la simulacion
	__link_changes:bool
	__trace_level:int
	__event_list:EventList

	# Data usada para la simulacion
	__entity:[Entity]
	__cost:[[int]]
	__time:float

	def __init__(self, has_link_change:bool, trace:int, s:int, num_entities, network_links):
		self.__link_changes = has_link_change
		self.__trace_level = trace
		self.__event_list = EventListImpl()
		self.__time = 0.0
		self.__netwkor_links = network_links
		self.__num_entities = num_entities
		seed(s)

		self.__initizalize_cost_matrix()

		self.__prepare_nodes()

		if self.__link_changes:
			self.__event_list.add(Event(10000.0, LINK_CHANGE, 0))


	'''
	Ejecuta el simlador de red. Todos los paquetes que son enviados, se procesan
	y envían a sus respectivos nodos destino.
	'''
	def run_simulator(self) -> None:
		next_event:Event
		packet:Packet

		while True:
			next_event = self.__siguiente_evento()

			if self.__sin_eventos_a_procesar(next_event):
				break

			if self.__logueo_basico():
				self.__logueo_informacion_packete(next_event)

			self.__obtener_tiempo_del_evento(next_event)

			if self.__evento_proviene_capa_dos(next_event):
				self.__procesar_evento_de_capa_dos(next_event)
			elif self.__evento_proviene_cambio_enlace(next_event):
				self.__procesar_evento_de_cambio_enlace()
			else:
				self.__procesar_evento_desconocido()

		if self.__logueo_basico():
			print('Simulador terminated at t=' + str(self.__time) + ', no packets in medium')
		
		if self.__logueo_maximo():
			self.__print_table()


	'''
	Devuelve el costo de un enlace en la matriz de costo
	'''
	def get_cost(self, i:int, j:int) -> int:
		return self.__cost[i][j]


	'''
	Procesa los paquetes encolados en la red y los procesa para enviarlos
	a sus respectivos destinos
	'''
	def to_layer_2(self, p):
		if self.__control_de_errores(p):
			return

		if self.__logueo_maximo():
			self.__log_costs_for_incomming_packet(p)

		arrival_time = self.__ultimo_elemento_en_llegar(p.get_source(), p.get_dest())

		if self.__logueo_maximo():
			print('to_layer_2(): Scheduling arrival of packet.')

		self.__enviar_ultimo_paquete(arrival_time, p)


	def obtener_costos(self):
		return [self.__entity[enlace].obtener_tabla() for enlace in range(self.__num_entities)]


	def numero_entidades(self):
		return self.__num_entities


	def __siguiente_evento(self):
		return self.__event_list.remove_next()


	def __sin_eventos_a_procesar(self, next_event):
		return next_event == None


	def __logueo_basico(self):
		return self.__trace_level > 1


	def __logueo_informacion_packete(self, next_event):
		print("\n")
		print('main(): event received. t=' + \
				str(next_event.get_time()) +  ', node=' + \
				str(next_event.get_entity()))

		if (next_event.get_type() == FROM_LAYER_2):
			packet = next_event.get_packet()
			msg = 'src=' + str(packet.get_source()) + ', '
			msg += 'dest=' + str(packet.get_dest()) + ', ' 
			msg += 'contest=['
			for i in range(self.__num_entities-1):
				msg += str(packet.get_min_cost(i)) + ', '
			msg += str(packet.get_min_cost(self.__num_entities - 1)) + ']' 
			print(msg)

		elif next_event.get_type() == LINK_CHANGE:
			print('  Link cost change')


	def __obtener_tiempo_del_evento(self, next_event):
		self.__time = next_event.get_time()


	def __evento_proviene_capa_dos(self, next_event):
		return next_event.get_type() == FROM_LAYER_2


	def __evento_proviene_cambio_enlace(self, next_event):
		return next_event.get_type() == LINK_CHANGE


	def __procesar_evento_de_capa_dos(self, next_event):
		packet = next_event.get_packet()

		if (next_event.get_entity() < 0 or 
			next_event.get_entity() >= self.__num_entities):
			print('main(): Panic. Unknown event entity.\n')
		else:
			self.__entity[next_event.get_entity()].update(packet)


	def __procesar_evento_desconocido(self):
		print('main(): Panic.  Unknown event type.\n')


	def __procesar_evento_de_cambio_enlace(self):
		if self.__time < 10001.0:
			self.__cost[0][1] = 20
			self.__cost[1][0] = 20
			self.__entity[0].link_cost_change_handler(1,1)
			self.__entity[1].link_cost_change_handler(0,1)


	def __print_table(self):
		self.__entity[0].print_DT()
		self.__entity[1].print_DT()
		self.__entity[2].print_DT()
		self.__entity[3].print_DT()


	def __initizalize_cost_matrix(self):
		num_entities = self.__num_entities
		self.__cost = [[0] * num_entities for i in range(num_entities)]

		for i in range(num_entities):
			for j in range(num_entities):
				self.__cost[i][j] = self.__netwkor_links[i][j]


	def __prepare_nodes(self):
		self.__entity = [0] * self.__num_entities
		for id in range(self.__num_entities):
			self.__entity[id] = Entity(id, self);


	def __source_out_of_range(self, p):
		return (p.get_source() < 0) or (p.get_source() >= self.__num_entities)


	def __destination_out_of_range(self, p):
		return (p.get_dest() < 0) or (p.get_dest() >= self.__num_entities)


	def __destination_is_source(self, p):
		return p.get_source() == p.get_dest()


	def __not_exists_link(self, p):
		return self.__cost[p.get_source()][p.get_dest()] == 999


	def __logueo_maximo(self):
		return self.__trace_level > 2


	def __log_costs(self, p):
		print('to_layer_2(): source=' + str(p.get_source()) + ' dest=' + str(p.get_dest()))
		print('				costs')

		result = ''
		for i in range(self.__num_entities):
			result += ' ' + str(self.__entity[i].get_min_cost(i))

		print(result)


	def __ultimo_elemento_en_llegar(self, source, dest):
		arrival_time = self.__event_list.get_last_packet(source, dest)

		if arrival_time == 0.0:
			arrival_time = self.__time

		arrival_time += 1.0 + (round(random(), 2)) * 9.0

		return arrival_time


	def __enviar_ultimo_paquete(self, arrival_time, p):
		current_packet = p.from_packet()
		self.__event_list.add(Event(arrival_time, FROM_LAYER_2,
			current_packet.get_dest(), current_packet))


	def __control_de_errores(self, p):
		hubo_errores = False
		
		if self.__source_out_of_range(p) or self.__destination_out_of_range(p):
			if self.__logueo_basico():
				print('to_layer_2(): WARNING: Illegal source or destination id in packet; ignoring.')
			hubo_errores = True

		elif self.__destination_is_source(p):
			if self.__logueo_basico():
				print('to_layer_2(): WARNING: Identical source and destination in packet; ignoring.')
			hubo_errores = True

		elif self.__not_exists_link(p):
			if self.__logueo_basico():
				print('to_layer_2(): WARNING: Source and destination not connected; ignoring.')
			hubo_errores = True

		return hubo_errores


if __name__ == "__main__":
	ns = NetworkSimulator(False, 0, 0)
	ns.run_simulator()
	print(ns.obtener_costos())
