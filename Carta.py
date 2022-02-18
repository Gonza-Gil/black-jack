# Clase para representar a las cartas

class Carta(object):
    
    RANGOS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    PALOS = ["c", "t", "p", "d"] # Corazon, Trebol, Pica y Diamante
    
    def __init__(self, rango, palo, cara_arriba = True):
        self.rango = rango 
        self.palo = palo
        self.is_cara_arriba = cara_arriba
        
    def __str__(self):
        if self.is_cara_arriba:
            cadena = self.rango + self.palo
        else:
            cadena = "XX"
        return cadena

    def flip(self):
        self.is_cara_arriba = not self.is_cara_arriba