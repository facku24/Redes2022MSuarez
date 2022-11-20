from sys import exit
from Constantes import *

class Packet:
    __source: int
    __dest: int
    __min_cost: [int]


    def __init__(self, s:int, d:int, mc:[int]):
        self.__num_entites = len(mc)
        self.__source = s
        self.__dest = d
        self.__min_cost = [0] * self.__num_entites

        if len(mc) != self.__num_entites:
            print('Packet(): Invalid data format.\n')
            exit(1)

        for i in range(self.__num_entites):
            self.__min_cost[i] = mc[i]


    def from_packet(self):
        mc = [0] * self.__num_entites

        for i in range(self.__num_entites):
            mc[i] = self.__min_cost[i]

        return Packet(self.__source,self.__dest, mc)


    def get_source(self) -> int:
        return self.__source


    def get_dest(self) -> int:
        return self.__dest


    def get_min_cost(self, ent:int) -> int:
        return self.__min_cost[ent]


    def get_min_costs(self):
        return self.__min_cost


    def to_string(self) -> str:
        string:str = 'source: ' + str(self.__source) + '  dest: ' + str(self.__dest) + '  mincosts: '

        for i in range(self.__num_entites):
            string += str(i) + '=' + str(self.get_min_cost(i)) + ' '

        return string