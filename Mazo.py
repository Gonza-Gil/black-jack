# Clase para representar el mazo de cartas

from random import random
from Carta import Carta
from Mano import Mano

class Mazo(Mano):
    
    def armar(self):
        for palo in Carta.PALOS:
            for rango in Carta.RANGOS:
                self.add(Carta(rango, palo))
                
    def mezclar(self):
        random.shuffle(self.cartas)
        
    def repartir(self, manos, cant_ronda):
        for ronda in range(cant_ronda):
            for mano in manos:
                if self.cartas:
                    carta_actual = self.cartas[0]
                    self.give
                    