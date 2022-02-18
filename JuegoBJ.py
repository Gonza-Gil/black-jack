from CrupierBJ import CrupierBJ
from JugadorBJ import JugadorBJ
from MazoBJ import MazoBJ


class JuegoBJ(object):
    
    def __init__(self, nombres):
        self.jugadores = []
        for nombre in nombres:
            jugador = JugadorBJ(nombre)
            self.jugadores.append(jugador)
        self.crupier = CrupierBJ("Crupier")
        self.mazo = MazoBJ()
        self.mazo.armar()
        self.mazo.mezclar()
        
    @property
    def siguen_jugando(self):
        sj = []
        for jugador in self.jugadores:
            if not jugador.se_paso():
                sj.append(jugador)
        return sj
    
    def __mas_cartas(self, jugador):
        while not jugador.se_paso() and jugador.is_pidiendo():
            self.mazo.repartir([jugador])
            print(jugador)
            if jugador.se_paso():
                jugador.perder()
                
    def jugar(self):
        # Reparte las primeras dos cartas
        self.mazo.repartir(self.jugadores + [self.crupier], cant_ronda=2)
        self.crupier.voltear_carta()    # Oculto la primer carta del Crupier
        for jugador in self.jugadores:
            print(jugador)
        print(self.crupier)
        
        # Dar mas cartas a cada jugador
        for jugador in self.jugadores:
            self.__mas_cartas(jugador)
            
        self.crupier.voltear_carta() # Muestro la primer carta del Crupier
        
        if not self.siguen_jugando:
            # Si no queda nadie jugando, muestro las cartas del Crupier
            print(self.crupier)
        else:
            print(self.crupier)
            self.__mas_cartas(self.crupier)
            
            if self.crupier.se_paso():
                # Si el Crupier pierde, todos los que siguen en juego ganan
                for jugador in self.siguen_jugando:
                    jugador.ganar()
            else:
                # Si el crupier sigue en juego, comparo los que siguen jugando con el crupier
                for jugador in self.siguen_jugando:
                    if jugador.total > self.crupier.total:
                        jugador.ganar()
                    elif jugador.total < self.crupier.total:
                        print(f'{jugador.name} pierda contra el Crupier.')
                    else:
                        print(f'{jugador.name} empata con el Crupier.')
        
        # Retiro las cartas de los jugadores
        for jugador in self.jugadores:
            jugador.clear()
        self.crupier.clear()
        
        
def main():
    print("\t\tBienvenido a Blackjack!\n")
    nombres = []
    num = int(input("Cuantos jugadores? (1 - 7): "))
    for i in range(num):
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)
    print()
    game = JuegoBJ(nombres)
    again = None
    while again != "n":
        game.jugar()
        again = input("Desea jugar otra vez? (S/N):").lower()
    
main()
input("\n\nPresione enter para salir.")