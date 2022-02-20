# Clase para representar el mazo de cartas

import random
from Carta import Carta
from Mano import Mano

class Mazo(Mano):
    
    # Armar llena inicialmente el mazo con todas las cartas
    def armar(self):
        for palo in Carta.PALOS:
            for rango in Carta.RANGOS:
                self.add(Carta(rango, palo))
                
    def mezclar(self):
        random.shuffle(self.cartas)
        
    # Repartir recibe como parametros un arreglo del tipo Mano, y un entero que indica la cantidad de cartas a repartir
    def repartir(self, manos, cant_ronda = 1):
        for ronda in range(cant_ronda):
            for mano in manos:
                if self.cartas:
                    carta_actual = self.cartas[0]
                    self.dar(carta_actual, mano)
                else:
                    print("No se puede seguir repartiendo, no hay mas cartas")
                    