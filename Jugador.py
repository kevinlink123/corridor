from Personaje import Personaje


class Jugador(Personaje):
    def __init__(self):
        Personaje.__init__(self)
        self.salud = 10
        self.saludMax = 10
        self.nombre = input("Cual es el nombre de tu personaje? ")
        print('')