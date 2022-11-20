from EventList import *

class EventListImpl(EventList):
	__data : [Event]


	def __init__(self):
		self.__data = []


	def add(self, e:Event) 	-> bool:
		#print('Adding... ' + e.to_string())
		self.__data.append(e)
		return True

	def remove_next(self) 	-> Event:

		if len(self.__data) == 0:
			return None

		firstIndex	: int 	= 0
		first 		: float = self.__at(firstIndex).get_time()

		for i in range(1, len(self.__data)):
			if self.__at(i).get_time() < first:
				first = self.__at(i).get_time()
				firstIndex = i

		next_elem:Event = self.__at(firstIndex)
		self.__data = self.__data[:firstIndex] + self.__data[firstIndex+1:]

		return next_elem


	def to_string(self) 	-> str:
		return str(self.__data)


	def get_last_packet(self, entity_from:int, entity_to:int) -> float:
		time:float = 0.0

		for i in range(len(self.__data)):
			if ((self.__at(i).get_type() == FROM_LAYER_2) and 
				(self.__at(i).get_entity() == entity_to) and 
				(self.__at(i).get_packet().get_source() == entity_from)):
				time = self.__at(i).get_time()

		return time


	def __at(self, index:int) -> Event:
		return self.__data[index]
