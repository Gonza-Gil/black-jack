from Carta import Carta

class CartaBJ(Carta):
    
    VALOR_AS = 1
    
    @property
    def valor(self):
        if self.is_cara_arriba:
            # Determino el valor de la carta basandome en su posición en el arreglo RANGOS de la clase Carta
            v = CartaBJ.RANGOS.index(self.rango) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v