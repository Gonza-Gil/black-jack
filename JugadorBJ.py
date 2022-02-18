from ManoBJ import ManoBJ

class JugadorBJ(ManoBJ):
    
    def is_pidiendo(self):
        respuesta = input(f'{self.name}, queres otra carta? (S/N):').lower()
        while respuesta not in ("s", "n"):
            respuesta = input(f'{self.name}, queres otra carta? (S/N):').lower()
        return respuesta == "s"
    
    def perder(self):
        print(f'{self.name} se pasó de 21. {self.name} pierde.')
        
    def ganar(self):
        print(f'{self.name} gana.')
