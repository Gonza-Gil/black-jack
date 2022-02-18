<h1> Black Jack </h1>

Juego de cartas "Black Jack" implementado en Python con el fin de aprender POO.<br>

## Jugar
_Para ejecutarlo correr en consola:_<br>
```
python JuegoBJ.py
```

## Desarrollo del juego
<p>El crupier reparte dos cartas visibles a cada jugador. El valor del As es 11 o +1, las figuras valen 10, y las cartas numéricas su valor original. El valor del As puede cambiarse
según la necesidad de no pasarse del número 21. Si a un jugador le sale un As junto con una carta de valor 10, obtiene blackjack automáticamente, ganando la apuesta salvo que el
crupier obtenga también blackjack. Al terminar de repartir las dos primeras cartas a cada jugador, el crupier pondrá luego su primera carta boca arriba de manera que sea visible
para el resto de jugadores, quienes podrán tomar sus decisiones en función de esa carta, mientras que el crupier tendrá una segunda carta boca abajo en espera de su turno. Cada
jugador compite únicamente contra el crupier, siendo indiferente a las cartas que tengan el resto de los demás jugadores. </p>

<p>Cada jugador tiene la posibilidad de plantarse y quedarse con cualquier puntuación, o de pedir más cartas hasta alcanzar los 21 puntos. Alcanzar los 21 puntos con más de una carta
extra no se considera blackjack, siendo por tanto esa jugada inferior al blackjack con dos cartas. Si al pedir una nueva carta se pasa de 21, el jugador pierde automáticamente la
partida y sus cartas y apuesta serán retiradas por el crupier. Cuando todos los jugadores hayan pedido sus cartas, el crupier mostrará su segunda carta boca abajo y sacará más
cartas si fuera necesario hasta sumar 17 o más puntos para alcanzar el número 21, momento en el que se plantará.</p>

<p>Entre el crupier y cada jugador, gana finalmente quién obtenga blackjack (As+10) o quien tenga la puntuación más alta sin pasarse de los 21 puntos, habiendo la posibilidad de
empate.</p>

## Implementación: clases base

Primero empecé creando las tres clases base: [Carta](Carta.py), [Mano](Mano.py) y [Mazo](Mazo.py). 

###### Carta

Cada carta cuenta con un valor (As, número, J, Q o K), un palo (Corazón, Diamante, Trébol o Pica) y un atributo que permite determinar si la carta esta cara arriba o cara abajo.
Como comportamiento tiene la implementación del metodo str y un metodo __flip__ que permite "dar vuelta" una carta.

###### Mano

Una mano es un conjunto de cartas, es por esto que la clase __Mano__ cuenta con el atributo cartas, que es un arreglo de objetos de tipo Carta.
Como comportamiento tiene la implementacion del metodo str, el metodo __clear__ que permite vaciar la Mano, el metodo __add__ que permite agregar cartas a la Mano y el metodo __dar__ que permite pasar una carta a otra Mano.

###### Mazo

Un Mazo no es más que una Mano que contiene todas las cartas en un principio, es por esto que hereda de la clase __Mano__. La clase __Mazo__ no tiene atributos propios, solo aquellos heredados de la clase __Mano__.
Como comportamiento tiene la implementación del metodo __armar__ que permite cargar todas las cartas en el mazo, el metodo __mezclar__ y el metodo __repartir__ que permite dar cartas a otras manos.
