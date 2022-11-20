from Packet import *

class Event:
	__time 		: float
	__type 		: float
	__entity	: int
	__packet 	: Packet

	def __init__(self, time:float, ty:int, entity:int, packet:Packet=None):
		self.__time 	= round(time, 2)
		self.__type		= ty
		self.__entity 	= entity

		if packet == None:
			self.__packet 	= None
		else :
			self.__packet 	= Packet.from_packet(packet)


	def set_time(self, time:float) -> bool:
		self.__time = time
		return True


	def set_type(self, n:int) -> bool:
		if n != FROM_LAYER_2 and n != LINK_CHANGE :
			self.__type = -1
			return False

		self.__type = n
		return True


	def set_entity(self, n:int) -> bool:
		num_entities = len(self.__packet.get_min_cost())
		if n < 0 or n >= num_entities:
			self.__entity = -1
			return False

		self.__entity = n
		return True


	def set_packet(p:Packet) -> bool:
		if p == None:
			self.__packet = None
		else:
			self.__packet = Packet.from_packet(p)

		return True


	def get_time(self) -> float:
		return self.__time


	def get_type(self) -> int:
		return self.__type


	def get_entity(self) -> int:
		return self.__entity

	def get_packet(self) -> Packet:
		return self.__packet

	def to_string(self) -> str:
		return  'time: ' + str(self.__time) + \
			 	'  type: ' + str(self.__type) + \
			 	'  entity: ' + str(self.__entity) + \
			 	'  packet: ' + self.__packet.to_string()

