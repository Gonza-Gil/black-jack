from ManoBJ import ManoBJ

class CrupierBJ(ManoBJ):
    
    def is_pidiendo(self):
        # El Crupier pide carta mientras su total sea menor a 17
        return self.total < 17
    
    def perder(self):
        print(f'{self.name} se pasó de 21. {self.name} pierde.')
 
    def voltear_carta(self):
        primer_carta = self.cartas[0]
        primer_carta.flip()