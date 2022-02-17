# Clase para representar a las cartas

class Carta(object):
    
    RANGOS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    PALOS = ["c", "t", "p", "d"] # Corazon, Trebol, Pica y Diamante
    
    def __init__(self, rango, palo):
        self.rango = rango 
        self.palo = palo
        
    def __str__(self):
        return self.rango + self.palo