from CartaBJ import CartaBJ
from Mano import Mano


class ManoBJ(Mano):
    def __init__(self, name):        
        super(ManoBJ, self).__init__()
        self.name = name
        
    def __str__(self):
        cadena = self.name + ":\t" + super(ManoBJ, self).__str__()
        if self.total:
            cadena += "(" + str(self.total) + ")"
        return cadena
    
    @property
    def total(self):
        # Si una carta en la mano contiene None, entonces el total es None
        for carta in self.cartas:
            if not carta.valor:
                return None
            
        # Sumo el valor de las cartas, los ases los cuento como uno
        t = 0
        for carta in self.cartas:
            t += carta.valor
            
        # Determino si la mano contiene ases
        contiene_as = False
        for carta in self.cartas:
            if carta.valor == CartaBJ.VALOR_AS:
                contiene_as = True
                
        # Si la mano contiene un as y el total es lo suficientemente bajo, trato el As como 11
        if contiene_as and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10
            
        return t
     
    def se_paso(self):
        return self.total > 21
    