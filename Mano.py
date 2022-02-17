# Clase para representar una mano

class Mano(object):
    
    def __init__(self):
        self.cartas = []
        
    def __str__(self):
        cadena = ""
        if self.cartascartas:
            for c in self.cartas:
                cadena += str(c) + " "
        else:
            cadena = "<Vacia>"
        return cadena
    
    def clear(self):
        self.cartas = []
        
    def add(self, carta):
        self.cartas.append(carta)