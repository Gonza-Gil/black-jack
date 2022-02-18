from CartaBJ import CartaBJ
from Mazo import Mazo

class MazoBJ(Mazo):
    
    def armar(self):
        for palo in CartaBJ.PALOS:
            for rango in CartaBJ.RANGOS:
                self.add(CartaBJ(rango, palo))